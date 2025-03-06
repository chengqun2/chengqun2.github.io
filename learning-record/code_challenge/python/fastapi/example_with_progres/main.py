from fastapi import FastAPI, HTTPException
import uvicorn
from typing import List
from pydantic import BaseModel
import asyncpg
from fastapi import HTTPException

app = FastAPI()

# Database configuration
DATABASE_URL = "postgresql://postgres:123456@localhost:5433/postgres"  # Update with your credentials


async def init_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        # Create users table if it doesn't exist
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            )
        ''')
    finally:
        await conn.close()

@app.on_event("startup")
async def startup_event():
    await init_db()

class User(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/", response_model=UserResponse)
async def create_user(user: User):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        row = await conn.fetchrow(
            "INSERT INTO users (name, email) VALUES ($1, $2) RETURNING id",
            user.name, user.email
        )
        return {"id": row['id'], "name": user.name, "email": user.email}
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Email already exists")
    finally:
        await conn.close()

@app.get("/users/", response_model=List[UserResponse])
async def read_users():
    conn = await asyncpg.connect(DATABASE_URL)
    rows = await conn.fetch("SELECT * FROM users")
    await conn.close()
    return [{"id": row['id'], "name": row['name'], "email": row['email']} for row in rows]

@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int):
    conn = await asyncpg.connect(DATABASE_URL)
    row = await conn.fetchrow("SELECT * FROM users WHERE id = $1", user_id)
    await conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": row['id'], "name": row['name'], "email": row['email']}

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: User):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        row = await conn.fetchrow(
            "UPDATE users SET name = $1, email = $2 WHERE id = $3 RETURNING *",
            user.name, user.email, user_id
        )
        if row is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"id": row['id'], "name": row['name'], "email": row['email']}
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Email already exists")
    finally:
        await conn.close()

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    conn = await asyncpg.connect(DATABASE_URL)
    row = await conn.execute("DELETE FROM users WHERE id = $1", user_id)
    await conn.close()
    if row == "DELETE 0":
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
