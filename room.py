from datetime import date
from typing import List
import asyncio

#note about rooms:
##SUITE: persons 1-4, $200 per night
##DOUBLE: persons 1-4, $125 per night
##SINGLE: persons 1, $75 per night


class Room:
    def __init__(self, room_id: int, price: int, persons: int, date_available_from: date, check_in: date = None, check_out: date = None):
       #initializes attributes 
       self.room_id = room_id #unique id for room
        self.price = price #price of room
        self.persons = persons #number of people who can fit in a room
        self.date_available_from = date_available_from #what days can the room be booked
        self.booked_dates = []  #list to stor dates room is booked for 
       #initialize empty list to store booked dates 
        self.check_in = check_in #check in date (start with none)
        self.check_out = check_out #check out date (start with none)
        
#convert to and from dictionary 
    def to_dict(self):
         #converts a room object into a dictionary
        return {
            "room_id": self.room_id,
            "price": self.price,
            "persons": self.persons,
            "date_available_from": self.date_available_from,
            "booked_dates": self.booked_dates,
            "check_in": self.check_in,
            "check_out": self.check_out
        }
   

    @classmethod
    async def from_dict(cls, data):
        #creates a room object from dictionary
        return cls(
            room_id=data['room_id'],
            price=data['price'],
            persons=data['persons'],
            date_available_from=data['date_available_from'],
            check_in=data.get('check_in'),
            check_out=data.get('check_out')
        )
    
#database operationz
    async def save_to_db(self, db):
        #saves the room object to database
        #inserts document if it doesnt exist
        await db.rooms.update_one({"room_id": self.room_id}, {"$set": self.to_dict()}, upsert=True)

    @staticmethod
    async def load_from_db(db, room_id):
        #load a room object from database using room id
        data = await db.rooms.find_one({"room_id": room_id})
        if data:
            return await Room.from_dict(data)
        return None



    @staticmethod
    async def load_all_from_db(db):
        #loads all rooms from database 
        rooms = []
        async for data in db.rooms.find():
            rooms.append(await Room.from_dict(data))
        return rooms

#booking a room
    async def book_room(self, check_in: date, check_out: date, db):
        #book the room if it is available for the given dates 
        #check availability 
        #add dates to the booked dates list then save updated data in database 
        if self.is_available(check_in, check_out):
          
            current_date = check_in
            while current_date < check_out:
                self.booked_dates.append(current_date)
                current_date += timedelta(days=1)
            await self.save_to_db(db)
            return True
        return False



    def is_available(self, check_in: date, check_out: date) -> bool:
          #check if room is available for the given dates by ensurinf there are no overlapping dates in booked _dates
        for booked_date in self.booked_dates:
            if (check_in <= booked_date < check_out) or (booked_date <= check_in < check_out):
                return False
        return True
    

#initiallizing rooms
async def initialize_rooms(db):
    #create and save rooms to da database based on predefined types and IDSs
    #set of rooms
    room_types = [
        {"type": "Suite", "price": 200, "persons": 4, "range": range(100, 105)},
        {"type": "Double", "price": 125, "persons": 4, "range": range(200, 205)},
        {"type": "Single", "price": 75, "persons": 1, "range": range(300, 305)}
    ]
    for room_type in room_types:
        for room_id in room_type["range"]:
            room = Room(room_id, room_type["price"], room_type["persons"], date.today())
            await room.save_to_db(db)


#execute the queen... haha jk,, main execute
db = asyncio.run(get_database())
asyncio.run(initialize_rooms(db)