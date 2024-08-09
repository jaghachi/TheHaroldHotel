from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from datetime import datetime

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
    
    async def insert_customer(self, newCustomer):
        
        db = await self.get_database()

        customers = db['customers']
        await customers.insert_one({
            "name": newCustomer.name, 
            "email": newCustomer.email, 
            "persons": newCustomer.persons
        })
        
        print(f"inserted - {newCustomer.name}" )
    
    async def insert_reservation(self, room, newCustomer, newReservation):
        
        db = await self.get_database()
        
        # Generate a unique reservation number
        reservation_number = "THH-" + str(datetime.now().strftime("%Y%m%d%H%M"))

        # Fetch the customer from db
        customer = await db['customers'].find_one({"email": newCustomer.email}) 
        
        
        # grab roomtype id to search for available rooms
        roomType = await db['roomTypes'].find_one({"type": room['type']}) 
        typeId = roomType['_id'] # type: ignore 
        
        # find open room based on type
        availableRoom = await db['rooms'].find_one({"typeId": typeId}) 

        #Insert into Reservations Collection
        reservations = db['reservations']
        await reservations.insert_one({
            "customerId": customer["_id"], # type: ignore 
            "roomId": availableRoom["_id"],  # Ensure you have the room ID here
            "confirmationNumber": reservation_number,
            "persons": newCustomer.persons,
            "checkIn": datetime(newReservation.checkIn.year(), newReservation.checkIn.month(), newReservation.checkIn.day()), # type: ignore
            "checkOut": datetime(newReservation.checkOut.year(), newReservation.checkOut.month(), newReservation.checkOut.day()) # type: ignore
        })
        
        return reservation_number
        
        

        

        
