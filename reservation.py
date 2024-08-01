from customer import Customer
from databaseFiles.databaseconnect import dataBase
from datetime import datetime
from reservation import Reservation

class Reservation:
    #object
    def __init__(self):
        self.customer = Customer()
        #customer info
        self.roomName = "" #name for resi 
        self.confirmationNumber = None #confirmation numb of resi
        self.persons = 0
        self.checkIn = None #checkin date
        self.checkOut = None #checkout date 

    
    def setCustomer(self, customer) -> None:
        self.customer = customer
        
    def getCustomer(self) -> Customer:
        #get customer 
        return self.customer
    
    def setRoomName(self, roomName) -> None:
        self.roomName = roomName
        
    def getRoomName(self) -> str:
        #get roomname 
        return self.roomName

    
    def getEmail(self) -> str:
        #get email of customer 
        return self.customer.email

    def getPrice(self) -> int:
        #get price of resi
        #to implement
        return 0
    
    def setPersons(self, customer) -> None:
        self.customer = customer

    def setConfirmation(self, confirmationNumber: int) -> None:
        #set confrimation number for resi
        self.confirmationNumber = confirmationNumber

    def modifyReservation(self, confirmationNumber: int) -> None:
        self.confirmationNumber = confirmationNumber
        # holder space for method
        #change or cancel resi based of confirmation number and user action to do so 

    def cancelReservation(self,confirmationNumber: int,) -> None:
        # holder method for cancel reservation logic
        pass

    async def reserveRoom(self, room, newReservation, adults, user_name, user_email) -> Reservation:
        #create databaseconnection
        db_instance = dataBase()
        db = await db_instance.get_database()
        
        #create customer
        newCustomer = Customer()
        newCustomer.set_name = user_name
        newCustomer.set_email = user_email
        newCustomer.set_persons = adults
        
        await db.insert_customer(newCustomer)
        
        # Fetch the customer from db
        customer = await db['customers'].find_one({"email": newCustomer.email})

        # Generate a unique reservation number
        reservation_number = "THH-" + str(datetime.now().strftime("%Y%m%d%H%M"))

        # Grab Reservations Collection
        reservations = db['reservations']
        
        # Insert reservation into the database
        await reservations.insert_one({
            "customerId": customer["_id"], # type: ignore 
            "roomId": room["_id"],  # Ensure you have the room ID here
            "confirmationNumber": reservation_number,
            "persons": adults,
            "checkIn": newReservation.checkin_date,  
            "checkOut": newReservation.checkout_date  
        })
        
        newReservation.setCustomer(newCustomer)
        newReservation.roomName = room["name"]
        newReservation.setConfirmation = reservation_number
        newReservation.setPersons = adults
        
        
        return newReservation