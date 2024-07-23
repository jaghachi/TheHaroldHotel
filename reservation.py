from datetime import date
from typing import List, Any

class Reservation:
    #object
    def __init__(self, customer: Any, email: str, persons: int, roomId: int, confirmationNumber: int, checkIn: date, checkOut: date):
        self.customer = customer
        #customer info
        self.email = email #customer email
        self.persons = persons #number of people for resi
        self.roomId = roomId #ID for resi 
        self.confirmationNumber = confirmationNumber #confirmation numb of resi
        self.checkIn = checkIn #checkin date
        self.checkOut = checkOut #checkout date 

    def getEmail(self) -> str:
        #get email of customer 
        return self.email

    def getPrice(self) -> int:
        #get price of resi
        # assume price calc logic is implemented somewhere else?
        # holder for actual price logic
        return 0

    def getPersons(self) -> int:
        #get number of people
        return self.persons

    def getDateAvailableFrom(self) -> date:
        #get next available date for resi
        # holer space for method
        return date.today()

    def getBookedDates(self) -> List[date]:
        #get booked dates for resi
        # holder space for method
        return [self.checkIn, self.checkOut]

    def setConfirmation(self, confirmationNumber: int) -> None:
        #set confrimation number for resi
        self.confirmationNumber = confirmationNumber

    def setPersons(self, persons: int) -> int:
        #set nmber of people for resi 
        self.persons = persons
        return self.persons

    def setDateAvailableFrom(self, dateAvailableFrom: date) -> None:
        #holder space for method
        #set next available date for resi
        pass

    def modifyReservation(self, confirmationNumber: int, modifyCancelReserve: str) -> None:
        self.confirmationNumber = confirmationNumber
        # holder space for method
        #change or cancel resi based of confirmation number and user action to do so 

    def cancelReservation(self) -> None:
        # holder method for cancel reservation logic
        pass

    def reserveRoom(self, id: int, price: int, persons: int, dateAvailableFrom: date, bookedDates: List[date]) -> None:
        self.roomId = id
        # Placeholder for reserve room logic
        #reserve a room with given details
        self.setPersons(persons)
        self.setDateAvailableFrom(dateAvailableFrom)
        self.bookedDates = bookedDates