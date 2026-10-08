from fastapi import FastAPI, Header, HTTPException, Request
import uvicorn

app = FastAPI(title="Mock National DPI Gateway")

@app.post("/v1/dpi/verify")
async def verify_transaction(request: Request, x_gateway_auth: str = Header(None)):
    if not x_gateway_auth:
        raise HTTPException(
            status_code=401, 
            detail="Missing required X-Gateway-Auth cryptographic signature."
        )
    
    payload = await request.json()
    return {
        "status": "SUCCESS",
        "txn_id": payload.get("txn_id", "SAMPLE_TXN_001"),
        "gateway_acknowledged": True
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)