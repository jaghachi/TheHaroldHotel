from datetime import date
from typing import List, Any
import random

#note:: dictionary for data base xoxx
#time to manage hotel reservations!!
class Reservation:
    #what the resi entails!!!
    def __init__(self, customer: Any, email: str, persons: int, room_id: int, check_in: date, check_out: date): #constructor method
        #initialization 
        #get cutomer info and their desired room and dates for hotel stay 
        self.customer = customer 
        self.email = email
        self.persons = persons
        self.room_id = room_id
        self.confirmation_number = random.randint(100000, 999999) #confirmation num will be random 
        self.check_in = check_in
        self.check_out = check_out


#convert to dictionary
    def to_dict(self):
        #change resi object into dictionary format
            #do this for da database 
        return {
         
            "customer": self.customer,
            "email": self.email,
            "persons": self.persons,
            "room_id": self.room_id,
            "confirmation_number": self.confirmation_number,
            "check_in": self.check_in,
            "check_out": self.check_out
        }

#create resi from dictionary
    @classmethod
    async def from_dict(cls, data):
#class method makes Reservation instance fromdictionary 
#asynchronous operation
        return cls(
            customer=data['customer'],
            email=data['email'],
            persons=data['persons'],
            room_id=data['room_id'],
            check_in=data['check_in'],
            check_out=data['check_out']
        )


#Save reservation to database 
    async def save_to_db(self, db):
        #add doc if it isn't there already 
        await db.reservations.update_one({"confirmation_number": self.confirmation_number}, {"$set": self.to_dict()}, upsert=True)

#load resi from database 
    @staticmethod
    async def load_from_db(db, confirmation_number):
        #if resi is found then create instance 
        data = await db.reservations.find_one({"confirmation_number": confirmation_number})
        if data:
            return await Reservation.from_dict(data)
        return None

#reserve room
    async def reserve_room(self, db, rooms):
        room = await Room.load_from_db(db, self.room_id)
        #load room from database 
        if room and await room.book_room(self.check_in, self.check_out, db):
            #book by dates 
            await self.save_to_db(db)
            #save resi to database if booked
            return True
        #successful
        return False
    #not successful 