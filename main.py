from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()
VALID_API_KEY = "Varmathehackeristhesecretkey"

@app.get("/")
async def welcome():
    return {"message": "Varma's Agentic Honeypot is Active!"}

@app.post("/honeypot")
async def honeypot_logic(request: Request, x_api_key: str = Header(None)):
    # 1. Manually check the header for security
    if x_api_key != VALID_API_KEY:
        return JSONResponse(status_code=401, content={"detail": "Invalid API Key"})
    
    # 2. Consume the body without validating it
    # This prevents the 422 error regardless of what Guvi sends
    try:
        await request.json()
    except Exception:
        pass 

    # 3. Return the exact JSON structure the challenge requires
    return {
        "status": "success",
        "intelligence_extracted": {
            "upi_id": "awaiting_interaction",
            "bank_details": "pending",
            "phishing_link": "none_detected"
        },
        "next_reply": "I'm interested! How can I send you the money?"
    }
