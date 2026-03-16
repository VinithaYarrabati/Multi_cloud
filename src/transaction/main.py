from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
import jwt

app = FastAPI()
SECRET_KEY = "multi-cloud-secret"

class TxnRequest(BaseModel):
    amount: float
    currency: str

def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Token expired or invalid")

@app.post("/txn/simulate")
def simulate(req: TxnRequest, user=Depends(verify_token)):
    return {
        "status": "success",
        "transaction_id": "TXN-999-EKS-AKS",
        "processed_by": user["sub"],
        "details": req
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
  
