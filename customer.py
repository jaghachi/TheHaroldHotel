from reservation import Reservation

class Customer:
    def __init__(self, name: str, email: str, persons: int, reservations: list):
        self.name = name
        self.email = email
        self.persons = persons
        self.reservations = reservations

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "persons": self.persons,
            "reservations": self.reservations
        }

    @classmethod
    async def from_dict(cls, data):
        return cls(
            name=data['name'],
            email=data['email'],
            persons=data['persons'],
            reservations=data['reservations']
        )

    async def save_to_db(self, db):
        await db.customers.update_one({"email": self.email}, {"$set": self.to_dict()}, upsert=True)

    @staticmethod
    async def load_from_db(db, email):
        data = await db.customers.find_one({"email": email})
        if data:
            return await Customer.from_dict(data)
        return None

    async def add_reservation(self, reservation: Reservation, db):
        self.reservations.append(reservation.confirmation_number)
        await self.save_to_db(db)

    async def review_reservation(self, confirmation_number: int, db):
        reservation = await Reservation.load_from_db(db, confirmation_number)
        if reservation:
            return f"Name: {self.name}, 
                    Dates: {reservation.get_dates()}, 
                    Room Type: {'Suite' if reservation.room_id < 200 else 'Double' if reservation.room_id < 300 else 'Single'}, 
                    Confirmation Number: {reservation.get_confirmation_number()}"
        return "Not Found"

    async def check_reservation(self, confirmation_number: int, db):
        reservation = await Reservation.load_from_db(db, confirmation_number)
        if reservation:
            return f"Reservation Found: Name: {self.name}, Room ID: {reservation.room_id}, Dates: {reservation.get_dates()}"
        return "Not Found"
        