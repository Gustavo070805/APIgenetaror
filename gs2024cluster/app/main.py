from fastapi import FastAPI
from app.routers import sensor_data

app = FastAPI()

app.include_router(sensor_data.router)

@app.get("/")
async def root():
    return {"message": "Coral Reef Monitoring API"}
