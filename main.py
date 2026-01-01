

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/alert")
def alert(message: str):
    return message
    # returnSONResponse(status=status.HTTP_200_OK, content= f"message:{message}")

