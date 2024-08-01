from datetime import date
from msilib.schema import CustomAction
from typing import List, Any
from customer import Customer

class Reservation:
    #object
    def __init__(self):
        self.customer = Customer()
        #customer info
        self.roomId = None #ID for resi 
        self.confirmationNumber = None #confirmation numb of resi
        self.price = 0
        self.checkIn = None #checkin date
        self.checkOut = None #checkout date 

    def getCustomer(self) -> Customer:
        #get customer 
        return self.customer
    
    def getEmail(self) -> str:
        #get email of customer 
        return self.customer.email

    def getPrice(self) -> int:
        #get price of resi
        return self.price

    def getPersons(self) -> int:
        #get number of people
        return self.customer.persons
    
    def setCustomer(self, customer) -> None:
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

    def reserveRoom(self, ) -> None:
        self.roomId = id
        # Placeholder for reserve room logic
        #reserve a room with given details