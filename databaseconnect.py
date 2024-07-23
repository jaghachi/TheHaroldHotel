import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

async def ping_server():
    # Replace the placeholder with your connection string
    uri = "mongodb://haroldAdmin:schoolProj@54.219.171.191:27017/theharoldhoteldb?authSource=admin"
    # Set the Stable API version when creating a new client
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print("Failed to connect:", e)

asyncio.run(ping_server())
