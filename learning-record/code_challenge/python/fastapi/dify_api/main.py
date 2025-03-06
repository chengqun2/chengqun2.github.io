from fastapi import FastAPI, HTTPException
import httpx
import json
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

# Configuration
DIFY_API_KEY = "app-h5HAMxK3x0mIcqpNct8Lq2p8"  # Replace with your actual API key
DIFY_API_URL = "http://127.0.0.1:8088/v1"

# Request model
class ChatRequest(BaseModel):
    query: str
    user: str

# Headers for Dify API
headers = {
    "Authorization": f"Bearer {DIFY_API_KEY}",
    "Content-Type": "application/json"
}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        async with httpx.AsyncClient() as client:
            payload = {
                "inputs": {},
                "query": request.query,
                "response_mode": "blocking",
                "conversation_id": "",
                "user": request.user
            }
            response = await client.post(
                f"{DIFY_API_URL}/chat-messages",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error from Dify API"
                )
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/chat-history")
async def get_chat_history(user: str, conversation_id: Optional[str] = None):
    try:
        async with httpx.AsyncClient() as client:
            url = f"{DIFY_API_URL}/messages?user={user}"
            if conversation_id:
                url += f"&conversation_id={conversation_id}"
                
            response = await client.get(
                url,
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error fetching chat history"
                )
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to Dify API wrapper"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)