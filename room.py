from datetime import date
from typing import List

#note about rooms:
##SUITE: persons 1-4, $200 per night
##DOUBLE: persons 1-4, $125 per night
##SINGLE: persons 1, $75 per night
class Room:
    def __init__(self, room_id: int, price: int, persons: int, date_available_from: date, check_in: date = None, check_out: date = None):
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



"""
### adding room descriptions 
rooms = []
#single
for i in range(100, 105):
    rooms.append(Room(room_id=i, price=200, persons=4, date_available_from=date.today()))

 #double
 for i in range(200, 205):
    rooms.append(Room(room_id=i, price=125, persons=4, date_available_from=date.today()))

#single
for i in range(300, 305):
    rooms.append(Room(room_id=i, price=75, persons=1, date_available_from=date.today()))

#room verify output
for room in rooms:
    print(f"Room ID: {room.get_id()}, Type: {'Suite' if room.get_price() == 200 else 'Double' if room.get_price() == 125 else 'Single'}, Price: {room.get_price()}, Max Persons: {room.get_persons()}, Available From: {room.get_date_available_from()}")
"""