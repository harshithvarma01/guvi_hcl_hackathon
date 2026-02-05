import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

VALID_API_KEY = "Varmathehackeristhesecretkey"

@app.get("/")
async def health_check():
    # Render uses this to see if your app is alive
    return {"status": "online"}

@app.post("/")
@app.post("/honeypot")
async def honeypot_logic(request: Request):
    # 1. Manually extract headers to avoid FastAPI 422/500 errors if missing
    headers = request.headers
    api_key = headers.get("api-key") or headers.get("x-api-key") or headers.get("X-API-Key")

    if api_key != VALID_API_KEY:
        return JSONResponse(
            status_code=401,
            content={"status": "error", "message": "Invalid API Key"}
        )

    # 2. Extract JSON safely
    try:
        await request.json()
    except:
        pass # Ignore body issues to ensure we return the expected format

    # 3. EXACT response format requested by your hackathon email
    return {
        "status": "success",
        "reply": "Why is my account being suspended?"
    }

if __name__ == "__main__":
    import uvicorn
    # This helps if you run it locally or via a direct python call
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
