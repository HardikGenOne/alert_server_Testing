

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from startlette.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

@app.post("/alert")
def alert(message: str):
    return message
    # returnSONResponse(status=status.HTTP_200_OK, content= f"message:{message}")

