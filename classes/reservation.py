"""
class: Reservation
most recent update: 8/13/2024
programmers: Janathan A and Macy V

Description:
"Reservation" class anages reservation details for a customer. 
    The class includes attributes for storing customer information, room details, and reservation-specific data like confirmation number, check-in, and check-out dates. 
    The class also provides methods for setting and retrieving these attributes, modifying or canceling reservations, and handling the reservation process with a database connection using asynchronous operations.
"""

from classes.customer import Customer
from databaseFiles.databaseconnect import dataBase
import pydoc

class Reservation:
    """
    A class to manage the reservation details for a customer.

    Attributes:
    -----------
    customer : Customer
        The customer associated with the reservation.
    roomName : str
        The name of the room reserved.
    confirmationNumber : str
        The confirmation number for the reservation.
    persons : int
        The number of persons included in the reservation.
    checkIn : datetime or None
        The check-in date for the reservation.
    checkOut : datetime or None
        The check-out date for the reservation.

    Methods:
    --------
    setCustomer(customer: Customer) -> None:
        Sets the customer for the reservation.
    getCustomer() -> Customer:
        Returns the customer associated with the reservation.
    setConfirmation(confirmationNumber: str) -> None:
        Sets the confirmation number for the reservation.
    getConfirmation() -> str:
        Returns the confirmation number of the reservation.
    setRoomName(roomName: str) -> None:
        Sets the name of the room for the reservation.
    getRoomName() -> str:
        Returns the name of the room reserved.
    getEmail() -> str:
        Returns the email address of the customer associated with the reservation.
    getPrice() -> int:
        Returns the price of the reservation (placeholder, returns 0).
    setPersons(persons: int) -> None:
        Sets the number of persons for the reservation.
    modifyReservation(confirmationNumber: str) -> None:
        Modifies the reservation based on the provided confirmation number.
    cancelReservation(confirmationNumber: str) -> None:
        Cancels the reservation based on the provided confirmation number.
    reserveRoom(room: dict, newCustomer: Customer, newReservation: dict) -> Reservation:
        Asynchronously reserves a room by inserting customer and reservation details into the database.
    """
    #object
    def __init__(self):
        """
        Initializes a Reservation object with default values for the customer, room name, confirmation number,
        number of persons, check-in date, and check-out date.
        """
        self.customer = Customer()
        #customer info
        self.roomName = "" #name for resi 
        self.confirmationNumber = "" #confirmation numb of resi
        self.persons = 0
        self.checkIn = None #checkin date
        self.checkOut = None #checkout date 

    
    def setCustomer(self, customer) -> None:
        """
        Sets the customer for the reservation.

        Parameters:
        -----------
        customer : Customer
            The customer object to be associated with the reservation.
        """
        self.customer = customer
        
    def getCustomer(self) -> Customer:
        """
        Returns the customer associated with the reservation.

        Returns:
        --------
        Customer
            The customer object associated with the reservation.
        """
        #get customer 
        return self.customer
    
    def setConfirmation(self, confirmationNumber: str):
        """
        Sets the confirmation number for the reservation.

        Parameters:
        -----------
        confirmationNumber : str
            The confirmation number to be assigned to the reservation.
        """
        #set confrimation number for resi
        self.confirmationNumber = confirmationNumber
    
    def getConfirmation(self):
        """
        Returns the confirmation number of the reservation.

        Returns:
        --------
        str
            The confirmation number of the reservation.
        """
        #set confrimation number for resi
        return self.confirmationNumber
    
    def setRoomName(self, roomName) -> None:
        """
        Sets the name of the room for the reservation.

        Parameters:
        -----------
        roomName : str
            The name of the room to be reserved.
        """
        self.roomName = roomName
        
    def getRoomName(self) -> str:
        """
        Returns the name of the room reserved.

        Returns:
        --------
        str
            The name of the room reserved.
        """
        #get roomname 
        return self.roomName

    
    def getEmail(self) -> str:
        """
        Returns the email address of the customer associated with the reservation.

        Returns:
        --------
        str
            The email address of the customer.
        """
        #get email of customer 
        return self.customer.email

    def getPrice(self) -> int:
        """
        Returns the price of the reservation.

        Note:
        -----
        This method is a placeholder and should be implemented with the actual logic for calculating the reservation price.

        Returns:
        --------
        int
            The price of the reservation (currently returns 0).
        """
        #get price of resi
        #to implement
        return 0
    
    def setPersons(self, persons) -> None:
        """
        Sets the number of persons for the reservation.

        Parameters:
        -----------
        persons : int
            The number of persons to be included in the reservation.
        """
        self.persons = persons

    def modifyReservation(self, confirmationNumber: str) -> None:
        """
        Modifies the reservation based on the provided confirmation number.

        Parameters:
        -----------
        confirmationNumber : str
            The confirmation number to be used for modifying the reservation.
        
        Note:
        -----
        This method is a placeholder for the logic to change or cancel a reservation.
        """
        self.confirmationNumber = confirmationNumber
        # holder space for method
        #change or cancel resi based of confirmation number and user action to do so 

    def cancelReservation(self,confirmationNumber: str,) -> None:
        """
        Cancels the reservation based on the provided confirmation number.

        Parameters:
        -----------
        confirmationNumber : str
            The confirmation number of the reservation to be canceled.
        
        Note:
        -----
        This method is a placeholder for the logic to cancel a reservation.
        """
        # holder method for cancel reservation logic
        pass

    async def reserveRoom(self, room, newCustomer, newReservation):
        """
        Asynchronously reserves a room by creating a database connection, inserting customer and reservation details.

        Parameters:
        -----------
        room : dict
            The room details to be reserved.
        newCustomer : Customer
            The customer making the reservation.
        newReservation : dict
            The reservation details.

        Returns:
        --------
        Reservation
            The updated Reservation object after the room has been reserved.
        """
        #create databaseconnection
        db_instance = dataBase()

        await db_instance.insert_customer(newCustomer)
        
        successful_reservation = await db_instance.insert_reservation(room, newCustomer, newReservation)

        
        self.setCustomer(newCustomer)
        self.setRoomName(room["name"])
        self.setConfirmation(successful_reservation)
        self.setPersons(newCustomer.persons)
        
        
        return self