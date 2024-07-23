from datetime import date
from typing import List

class Room:
    def __init__(self, room_id: int, price: int, persons: int, date_available_from: date, check_in: date, check_out: date):
        self.room_id = room_id
        self.price = price
        self.persons = persons
        self.date_available_from = date_available_from
        self.booked_dates = []
        self.check_in = check_in
        self.check_out = check_out

    def get_id(self) -> int:
        return self.room_id

    def get_price(self) -> int:
        return self.price

    def get_persons(self) -> int:
        return self.persons

    def get_date_available_from(self) -> date:
        return self.date_available_from

    def get_booked_dates(self) -> List[date]:
        return self.booked_dates

    def set_id(self, room_id: int):
        self.room_id = room_id

    def set_price(self, price: int):
        self.price = price

    def set_persons(self, persons: int):
        self.persons = persons

    def set_date_available_from(self, date_available_from: date):
        self.date_available_from = date_available_from

    def set_check_in(self, check_in: date):
        self.check_in = check_in

    def set_check_out(self, check_out: date):
        self.check_out = check_out
