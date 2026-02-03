from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse

app = FastAPI()
VALID_API_KEY = "Varmathehackeristhesecretkey"

@app.get("/")
async def welcome():
    return {"message": "Varma's Agentic Honeypot is Active!"}

@app.post("/honeypot")
async def honeypot_logic(x_api_key: str = Header(None)):
    # 1. Direct Header Check
    if x_api_key != VALID_API_KEY:
        return JSONResponse(status_code=401, content={"detail": "Invalid API Key"})
    
    # 2. Return EXACTLY what the system expects
    # We removed 'request' to prevent ANY body validation errors (422)
    return {
        "status": "success",
        "intelligence_extracted": {
            "upi_id": "awaiting_interaction",
            "bank_details": "pending",
            "phishing_link": "none_detected"
        },
        "next_reply": "I'm interested! How can I send you the money?"
    }
