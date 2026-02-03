from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

# This is your custom secret key for the Guvi portal
VALID_API_KEY = "Varmathehackeristhesecretkey" 

class ScamInput(BaseModel):
    message: str

# 1. Root Endpoint (Fixes the "Not Found" error on the home page)
@app.get("/")
async def welcome():
    return {"message": "Varma's Agentic Honeypot is Active! and for the local server it is http://127.0.0.1:8000/docs"}

# 2. Honeypot Logic (The actual challenge endpoint)
@app.post("/honeypot")
async def honeypot_logic(data: ScamInput, x_api_key: str = Header(None)):
    # Security Check: Verifies the key you enter in the Guvi portal
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    # JSON Response required by the problem statement
    return {
        "status": "success",
        "intelligence_extracted": {
            "upi_id": "awaiting_interaction",
            "bank_details": "pending",
            "phishing_link": "none_detected"
        },
        "next_reply": "I'm interested! How can I help you"
    }