

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


from pydantic import BaseModel

class AlertRequest(BaseModel):
    req: str

@app.post("/alert")
async def get_stock_symbol(data: AlertRequest):
    print("... MESSAGE RECEIVED ...")
    print(data.req)
    return {"message": data.req}
