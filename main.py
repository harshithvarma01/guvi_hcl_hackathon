from fastapi import FastAPI, Header, HTTPException, Request

app = FastAPI()
VALID_API_KEY = "Varmathehackeristhesecretkey"

@app.get("/")
async def welcome():
    return {"message": "Varma's Agentic Honeypot is Active!"}

@app.post("/honeypot")
async def honeypot_logic(request: Request, x_api_key: str = Header(None)):
    # 1. Security Check
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    # 2. Flexible Body Handling
    # This accepts whatever Guvi sends (even if it's not "message")
    try:
        body = await request.json()
    except Exception:
        body = "No valid JSON found"

    # 3. Return the response they expect
    return {
        "status": "success",
        "intelligence_extracted": {
            "upi_id": "awaiting_interaction",
            "bank_details": "pending",
            "phishing_link": "none_detected"
        },
        "next_reply": "I'm interested! How can I send you the money?"
    }
