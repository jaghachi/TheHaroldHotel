"""
class: Room
most recent update: 8/13/2024
programmers: Jonathan Aghachi and Macy V

Description: "Room" class represents a hotel room with attributes such as room ID, price, capacity (number of persons it can accommodate), availability date, and booking details like check-in and check-out dates. 
    The class provides methods to set and get these attributes. 

"""

from datetime import date
from typing import List
import pydoc

#note about rooms:
##SUITE: persons 1-4, $200 per night
##DOUBLE: persons 1-4, $125 per night
##SINGLE: persons 1, $75 per night
class Room:
    """
    A class to represent a hotel room with its details.

    Attributes:
    -----------
    room_id : int
        The unique identifier for the room.
    price : int
        The price of the room per night.
    persons : int
        The maximum number of persons the room can accommodate.
    date_available_from : date
        The date from which the room is available for booking.
    booked_dates : list of date
        A list of dates on which the room is already booked.
    check_in : date or None
        The check-in date for the current booking.
    check_out : date or None
        The check-out date for the current booking.

    Methods:
    --------
    get_id() -> int:
        Returns the unique ID of the room.
    get_price() -> int:
        Returns the price of the room per night.
    get_persons() -> int:
        Returns the maximum number of persons the room can accommodate.
    get_date_available_from() -> date:
        Returns the date from which the room is available for booking.
    get_booked_dates() -> List[date]:
        Returns the list of dates on which the room is booked.
    set_id(room_id: int) -> None:
        Sets the unique ID for the room.
    set_price(price: int) -> None:
        Sets the price of the room per night.
    set_persons(persons: int) -> None:
        Sets the maximum number of persons the room can accommodate.
    set_date_available_from(date_available_from: date) -> None:
        Sets the date from which the room is available for booking.
    set_check_in(check_in: date) -> None:
        Sets the check-in date for the current booking.
    set_check_out(check_out: date) -> None:
        Sets the check-out date for the current booking.
    """

    def __init__(self, room_id: int, price: int, persons: int, date_available_from: date, check_in: date = None, check_out: date = None):
        """
        Initializes a Room object with the given details.

        Parameters:
        -----------
        room_id : int
            The unique identifier for the room.
        price : int
            The price of the room per night.
        persons : int
            The maximum number of persons the room can accommodate.
        date_available_from : date
            The date from which the room is available for booking.
        check_in : date, optional
            The check-in date for the current booking (default is None).
        check_out : date, optional
            The check-out date for the current booking (default is None).
        """
        self.room_id = room_id #unique id for room
        self.price = price #price of room
        self.persons = persons #number of people who can fit in a room
        self.date_available_from = date_available_from #what days can the room be booked
        self.booked_dates = []  #list to stor dates room is booked for 
        self.check_in = check_in #check in date (start with none)
        self.check_out = check_out #check out date (start with none)
        
    def get_id(self) -> int:
        #get room id
        return self.room_id

    def get_price(self) -> int:
        #GET PRICE OF ROOM
        return self.price

    def get_persons(self) -> int:
        #get value of how many people can be in room
        return self.persons

    def get_date_available_from(self) -> date:
        #get what days the room is available 
        return self.date_available_from

    def get_booked_dates(self) -> List[date]:
        #get list of the dates room is booked
        return self.booked_dates

    def set_id(self, room_id: int):
        #set room id (unique)
        self.room_id = room_id

    def set_price(self, price: int):
        #set price of room
        self.price = price

    def set_persons(self, persons: int):
        #set umber of people in room
        self.persons = persons

    def set_date_available_from(self, date_available_from: date):
        #et avaibale dates 
        self.date_available_from = date_available_from

    def set_check_in(self, check_in: date):
        #set check in date
        self.check_in = check_in

    def set_check_out(self, check_out: date):
        #set check out date 
        self.check_out = check_out
        
        
rooms = [
        {"name": "Premiere Harold Single", "type": "Single", "sleeps": 1, "price": 75, "image": "resources/single.jpg"},
        {"name": "Premiere Harold Double", "type": "Double", "sleeps": 4, "price": 125, "image": "resources/double.jpg"},
        {"name": "Premiere Harold Suite", "type": "Suite", "sleeps": 4, "price": 200, "image": "resources/suite.jpeg"}
    ]