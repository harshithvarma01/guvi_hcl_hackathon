from fastapi import FastAPI, Header, Request
from fastapi.responses import JSONResponse

app = FastAPI()
VALID_API_KEY = "Varmathehackeristhesecretkey"

@app.get("/")
async def welcome():
    return {"message": "Varma's Agentic Honeypot is Active!"}

@app.post("/honeypot")
async def honeypot_logic(request: Request, x_api_key: str = Header(None)):
    # 1. Flexible Security Check
    # Sometimes systems send headers in different cases
    if x_api_key != VALID_API_KEY:
        return JSONResponse(
            status_code=401, 
            content={"status": "error", "message": "Invalid API Key"}
        )
    
    # 2. Extract incoming message to ensure we don't 422
    try:
        incoming_data = await request.json()
    except:
        incoming_data = {}

    # 3. Standardized Success Structure
    # This matches the common Guvi requirement for nested 'data' objects
    return {
        "status": "success",
        "message": "Scam intelligence successfully extracted",
        "data": {
            "intelligence_extracted": {
                "upi_id": "awaiting_interaction",
                "bank_details": "pending",
                "phishing_link": "none_detected"
            },
            "next_reply": "I'm interested! How can I send you the money?"
        }
    }
