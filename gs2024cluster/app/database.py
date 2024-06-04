from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://mongodb:27017")
db = client.coral_reef_monitoring
