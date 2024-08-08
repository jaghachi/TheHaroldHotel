from classes.customer import Customer
from databaseFiles.databaseconnect import dataBase

class Reservation:
    #object
    def __init__(self):
        self.customer = Customer()
        #customer info
        self.roomName = "" #name for resi 
        self.confirmationNumber = "" #confirmation numb of resi
        self.persons = 0
        self.checkIn = None #checkin date
        self.checkOut = None #checkout date 

    
    def setCustomer(self, customer) -> None:
        self.customer = customer
        
    def getCustomer(self) -> Customer:
        #get customer 
        return self.customer
    
    def setConfirmation(self, confirmationNumber: str):
        #set confrimation number for resi
        self.confirmationNumber = confirmationNumber
    
    def getConfirmation(self):
        #set confrimation number for resi
        return self.confirmationNumber
    
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
    
    def setPersons(self, persons) -> None:
        self.persons = persons

    def modifyReservation(self, confirmationNumber: str) -> None:
        self.confirmationNumber = confirmationNumber
        # holder space for method
        #change or cancel resi based of confirmation number and user action to do so 

    def cancelReservation(self,confirmationNumber: str,) -> None:
        # holder method for cancel reservation logic
        pass

    async def reserveRoom(self, room, newCustomer, newReservation):
        #create databaseconnection
        db_instance = dataBase()

        await db_instance.insert_customer(newCustomer)
        
        successful_reservation = await db_instance.insert_reservation(room, newCustomer, newReservation)

        
        self.setCustomer(newCustomer)
        self.setRoomName(room["name"])
        self.setConfirmation(successful_reservation)
        self.setPersons(newCustomer.persons)
        
        
        return self