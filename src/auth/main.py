from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
import datetime

app = FastAPI()
SECRET_KEY = "multi-cloud-secret" # In production, use environment variables

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(req: LoginRequest):
    # Mock authentication logic
    if req.username == "admin" and req.password == "password123":
        token = jwt.encode({
            "sub": req.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")
        return {"access_token": token, "token_type": "bearer"}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
  
