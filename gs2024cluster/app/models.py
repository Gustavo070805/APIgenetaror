from pydantic import BaseModel

class SensorData(BaseModel):
    temperature: dict
    dissolved_oxygen: dict
    salinity: dict
    turbidity: dict
    microplastics: dict
