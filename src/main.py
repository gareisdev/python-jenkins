from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
async def home():
    return {"message": "Hi Dev!"}


@app.get("/api/health")
async def health_check():
    return {"message": "OK"}
