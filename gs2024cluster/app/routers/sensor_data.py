from fastapi import APIRouter, HTTPException
from app.models import SensorData
from app.database import db

router = APIRouter(
    prefix="/sensor_data",
    tags=["sensor_data"],
)

@router.post("/")
async def create_sensor_data(sensor_data: SensorData):
    try:
        result = await db.sensor_data.insert_one(sensor_data.dict())
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
