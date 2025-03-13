from fastapi import FastAPI, HTTPException
import requests
import os
from typing import Dict, List
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configure Airtable credentials
AIRTABLE_API_KEY = "patWVddS4zQU1OJZT.a5aeb69467ace82e44223fe42392dd3b63c209afec4979cdcad83cc5eeb7b31b"
BASE_ID = "appldMc5FjQa1AOuG"
TABLE_NAME = "Students"

# Airtable API base URL
AIRTABLE_URL = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

@app.get("/records")
async def get_records() -> Dict:
    """Get all records from Airtable"""
    try:
        response = requests.get(AIRTABLE_URL, headers=headers)
        response.raise_for_status()
        
        # Log response for debugging
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response headers: {response.headers}")
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/records")
async def create_record(fields: Dict) -> Dict:
    """Create a new record in Airtable"""
    try:
        payload = {"records": [{"fields": fields}]}
        response = requests.post(AIRTABLE_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.patch("/records/{record_id}")
async def update_record(record_id: str, fields: Dict) -> Dict:
    """Update a record in Airtable"""
    try:
        payload = {"fields": fields}
        url = f"{AIRTABLE_URL}/{record_id}"
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/records/{record_id}")
async def delete_record(record_id: str) -> Dict:
    """Delete a record from Airtable"""
    try:
        url = f"{AIRTABLE_URL}/{record_id}"
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"message": "Record deleted successfully"}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)