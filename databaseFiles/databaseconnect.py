"""
class: dataBase
most recent update: 8/13/2024 (commenting)

Description: dataBase class that manages interactions with a MongoDB database using the asynchronous Motor library.

programmers: Jonathan Aghachi Macy V
"""

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from datetime import datetime
import pydoc

class dataBase:
    """
    A class to handle asynchronous operations with a MongoDB database.

    Attributes:
    -----------
    client : AsyncIOMotorClient
        The MongoDB client for database connection.
    db : AsyncIOMotorClient
        The specific database within MongoDB to interact with.

    Methods:
    --------
    ping_server() -> None:
        Pings the MongoDB server to check the connection.
    get_database() -> AsyncIOMotorClient:
        Retrieves the database object for performing operations.
    insert_customer(newCustomer: Customer) -> None:
        Inserts a new customer into the 'customers' collection.
    insert_reservation(room: dict, newCustomer: Customer, newReservation: Reservation) -> str:
        Inserts a new reservation into the 'reservations' collection and returns a confirmation number.
    """
    def __init__(self):
        """
        Initializes the dataBase object with default MongoDB client and database.
        """
        self.client = AsyncIOMotorClient()
        self.db = AsyncIOMotorClient()

    async def ping_server(self):
        """
        Pings the MongoDB server to verify a successful connection.

        This method attempts to connect to the MongoDB server using the provided URI and sends a ping command.
        If the connection is successful, a message is printed. Otherwise, an error message is displayed.
        """
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
        """
        Retrieves the MongoDB database object for performing operations.

        Connects to the MongoDB server using the provided URI and returns the specified database.
        
        Returns:
        --------
        AsyncIOMotorClient
            The database object to interact with.
        """
        uri = "mongodb://haroldAdmin:schoolProj@54.219.171.191:27017/theharoldhoteldb?authSource=admin"
        self.client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        self.db = self.client.theharoldhoteldb
        return self.db
    
    async def insert_customer(self, newCustomer):
        """
        Inserts a new customer into the 'customers' collection in the database.

        Parameters:
        -----------
        newCustomer : Customer
            The customer object containing the details to be inserted.
        """   
        db = await self.get_database()

        customers = db['customers']
        await customers.insert_one({
            "name": newCustomer.name, 
            "email": newCustomer.email, 
            "persons": newCustomer.persons
        })
        
        print(f"inserted - {newCustomer.name}" )
    
    async def insert_reservation(self, room, newCustomer, newReservation):
        """
        Inserts a new reservation into the 'reservations' collection in the database.

        Generates a unique reservation number and inserts the reservation details, linking the reservation
        to the corresponding customer and room.

        Parameters:
        -----------
        room : dict
            The room details for the reservation.
        newCustomer : Customer
            The customer making the reservation.
        newReservation : Reservation
            The reservation details.

        Returns:
        --------
        str
            The confirmation number of the new reservation.
        """     
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
        
    async def change_reservation(self,reservation,roomTypeName,checkIn,checkOut,adults):
        
        rooms = [
            {"name": "Premiere Harold Single", "type": "Single", "sleeps": 1, "price": 75, "image": "resources/single.jpg"},
            {"name": "Premiere Harold Double", "type": "Double", "sleeps": 4, "price": 125, "image": "resources/double.jpg"},
            {"name": "Premiere Harold Suite", "type": "Suite", "sleeps": 4, "price": 200, "image": "resources/suite.jpeg"}
        ]
        
        # Find the room by name
        # refractor to better code later
        room = next((room for room in rooms if room["name"] == roomTypeName), None)
        
        db = await self.get_database()
        
        # Fetch the reservation from db
        reservation = await db['reservations'].find_one({"confirmationNumber": reservation['confirmationNumber']}) 
        
        roomType = await db['roomTypes'].find_one({"type": room["type"]})
        
        fRoom =  await db['rooms'].find_one({"typeId": roomType["_id"]})
        
        # Define the fields you want to update
        update_fields = {
            "$set": {
                "persons": adults,
                "roomId": fRoom["_id"], # type: ignore
                "checkIn": datetime(checkIn.year(), checkIn.month(), checkIn.day()), # type: ignore
                "checkOut": datetime(checkOut.year(), checkOut.month(), checkOut.day()) # type: ignore
                
            }
        }

        # Update the reservation
        result = await db['reservations'].update_one({'_id': reservation['_id']}, update_fields)

        # Check if the update was successful
        if result.modified_count > 0:
            print("Reservation successfully updated.")
        else:
            print("No Reservation was updated.")  
    
        return result  

    async def cancel_reservation(self,reservation):
        db = await self.get_database()
        
        # Cancel the reservation from db
        await db['reservations'].delete_one({"_id": reservation['_id']})
       
 
        
        

        
