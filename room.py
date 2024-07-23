from datetime import date
from typing import List

class Room:
    def __init__(self, room_id: int, price: int, persons: int, date_available_from: date, check_in: date, check_out: date):
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
