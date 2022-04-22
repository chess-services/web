from fastapi import FastAPI
import uvicorn

from config import Settings

settings = Settings()
app = FastAPI()


@app.get("/")
def hello_world():
    return "Hello world"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.port, reload=True)
