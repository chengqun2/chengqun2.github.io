from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, HttpUrl
import shortuuid
from typing import Dict
from fastapi.testclient import TestClient
import uvicorn
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Allow CORS for React frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost:5433/postgres"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    logger.error(f"Database connection failed: {e}")
    raise

class URLMap(Base):
    __tablename__ = "orgin_shorten"
    short_id = Column(String, primary_key=True)
    target_url = Column(String)

# Dependency for database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    logger.error(f"Failed to create tables: {e}")
    raise

class URLInput(BaseModel):
    target_url: HttpUrl

class URLResponse(BaseModel):
    short_url: str
    target_url: str

@app.post("/shorten", response_model=URLResponse)
async def create_short_url(url_input: URLInput, db: Session = Depends(get_db)):
    try:
        short_id = shortuuid.uuid()[:8]
        url_map = URLMap(short_id=short_id, target_url=str(url_input.target_url))
        db.add(url_map)
        db.commit()
        
        return URLResponse(
            short_url=f"/r/{short_id}",
            target_url=str(url_input.target_url)
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating short URL: {e}")
        raise HTTPException(status_code=500, detail="Error creating short URL")

@app.get("/r/{short_id}")
async def redirect_url(short_id: str, db: Session = Depends(get_db)):
    try:
        url_map = db.query(URLMap).filter(URLMap.short_id == short_id).first()
        if not url_map:
            raise HTTPException(status_code=404, detail="URL not found")
        return {"url": url_map.target_url}
    except Exception as e:
        logger.error(f"Error retrieving URL: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving URL")

@app.get("/urls")
async def get_all_urls(db: Session = Depends(get_db)):
    try:
        urls = db.query(URLMap).all()
        return [{"short_id": url.short_id, "target_url": url.target_url} for url in urls]
    except Exception as e:
        logger.error(f"Error retrieving URLs: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving URLs")


# For testing purposes, you can save this in test_main.py
"""

client = TestClient(app)

def test_create_short_url():
    response = client.post(
        "/shorten",
        json={"target_url": "https://www.example.com"}
    )
    assert response.status_code == 200
    assert "short_url" in response.json()
    assert "target_url" in response.json()
    assert response.json()["target_url"] == "https://www.example.com"

def test_redirect_url():
    # First create a shortened URL
    response = client.post(
        "/shorten",
        json={"target_url": "https://www.example.com"}
    )
    short_url = response.json()["short_url"]
    
    # Test the redirect
    response = client.get(short_url)
    assert response.status_code == 200
    assert response.json()["url"] == "https://www.example.com"

def test_invalid_short_url():
    response = client.get("/r/invalid")
    assert response.status_code == 404
"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)