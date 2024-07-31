from motor.motor_asyncio import AsyncIOMotorClient # type: ignore
from pymongo.server_api import ServerApi # type: ignore

class dataBase:
    def __init__(self):
        self.client = None
        self.db = None

    async def ping_server(self):
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
        finally:
            client.close()
    
    async def get_database(self):
        if self.client is None:
            uri = "mongodb://haroldAdmin:schoolProj@54.219.171.191:27017/theharoldhoteldb?authSource=admin"
            self.client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
            self.db = self.client.theharoldhoteldb
        return self.db
    