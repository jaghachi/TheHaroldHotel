from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

class dataBase:
    def __init__(self):
        self.client = AsyncIOMotorClient()
        self.db = AsyncIOMotorClient()

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
            self.client.close()
    
    async def get_database(self):
        uri = "mongodb://haroldAdmin:schoolProj@54.219.171.191:27017/theharoldhoteldb?authSource=admin"
        self.client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        self.db = self.client.theharoldhoteldb
        return self.db
    
    async def insert_customer(self, customer):
        
        db_instance = self.get_database()
        db = await db_instance

        customers = db['customer']
        await customers.insert_one({
                "customer": {
                    "name": customer.name, 
                    "email": customer.email, 
                    "persons": customer.persons
                }
        })
    
    async def insert_reservation(self):
        
        db_instance = self.get_database()
        db = await db_instance

        # Find the customer
        customer = await db['customers'].find_one({"email": "john.doe@example.com"})

        # Create Reservations Collection
        reservations = db['reservations']
        await reservations.insert_one([
            {
                "customerId": customer["_id"], #type: ignore 
                "roomId": None,
                "confirmationNumber": "123456",
                "checkIn": None,
                "checkOut": None
            }
        ])