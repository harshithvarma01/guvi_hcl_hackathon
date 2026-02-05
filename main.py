from fastapi import FastAPI, Header, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Your specific API Key
VALID_API_KEY = "Varmathehackeristhesecretkey"

@app.get("/")
async def root():
    return {"status": "active", "message": "Honeypot is running"}

# Changed to handle the root or /honeypot depending on what you submitted
@app.post("/")
@app.post("/honeypot")
async def honeypot_logic(request: Request, x_api_key: str = Header(None), api_key: str = Header(None)):
    # Check both common header formats (X-API-Key and API-Key)
    provided_key = x_api_key or api_key
    
    if provided_key != VALID_API_KEY:
        return JSONResponse(
            status_code=401,
            content={"status": "error", "message": "Unauthorized"}
        )

    # The email says they send a JSON body; we must accept it even if we don't use it
    try:
        body = await request.json()
    except Exception:
        body = {}

    # EXACT format requested in your email
    return {
        "status": "success",
        "reply": "Why is my account being suspended?"
    }
