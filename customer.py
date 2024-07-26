from reservation import Reservation

class Customer:
    
    """
        Represents a customer who can have multiple reservations.

        Attributes:
            name (str): The name of the customer.
            email (str): The email address of the customer.
            persons (int): Number of persons the customer represents.
            reservations (list): List of reservation confirmation numbers.

        Methods:
            to_dict(): Converts the customer object to a dictionary.
            from_dict(data): Class method to create a customer object from a dictionary.
            save_to_db(db): Saves the customer object to the database.
            load_from_db(db, email): Static method to load a customer object from the database using the email.
            add_reservation(reservation, db): Adds a reservation to the customer's list and saves to the database.
            review_reservation(confirmation_number, db): Returns a formatted string with reservation details.
            check_reservation(confirmation_number, db): Returns a formatted string if the reservation is found.
    """
    
    
    def __init__(self, name: str, email: str, persons: int, reservations: list):
        """
            Initializes a new Customer instance.

            Args:
                name (str): The name of the customer.
                email (str): The email address of the customer.
                persons (int): Number of persons the customer represents.
                reservations (list): List of reservation confirmation numbers.
        """
        self.name = name
        self.email = email
        self.persons = persons
        self.reservations = reservations

    def to_dict(self):
        """
            Converts the customer object to a dictionary format.

            Returns:
                dict: A dictionary representation of the customer object.
        """
        
        return {
            "name": self.name,
            "email": self.email,
            "persons": self.persons,
            "reservations": self.reservations
        }

    @classmethod
    async def from_dict(cls, data):
        """
            Creates a Customer instance from a dictionary.

            Args:
                data (dict): A dictionary containing customer data for mongodb.

            Returns:
                Customer: A new Customer instance.
        """
        return cls(
            name=data['name'],
            email=data['email'],
            persons=data['persons'],
            reservations=data['reservations']
        )

    async def save_to_db(self, db):
        """
            Saves the customer object to the database.

            Args:
                db: The database connection object.
        """
        await db.customers.update_one({"email": self.email}, {"$set": self.to_dict()}, upsert=True)

    @staticmethod
    async def load_from_db(db, email):
        """
            Loads a customer object from the database using the email.

            Args:
                db: The database connection object.
                email (str): The email address of the customer.

            Returns:
                Customer or None: The Customer instance if found, otherwise None.
        """        
        
        data = await db.customers.find_one({"email": email})
        if data:
            return await Customer.from_dict(data)
        return None

    async def add_reservation(self, reservation: Reservation, db):
        """
            Adds a reservation to the customer's list and saves the updated list to the database.

            Args:
                reservation (Reservation): The reservation to be added.
                db: The database connection object.
        """
        self.reservations.append(reservation.confirmation_number)
        await self.save_to_db(db)

    async def review_reservation(self, confirmation_number: int, db):
        """
            Reviews a reservation and returns a formatted string with reservation details.

            Args:
                confirmation_number (int): The confirmation number of the reservation.
                db: The database connection object.

            Returns:
                str: A formatted string with reservation details or 'Not Found' if the reservation does not exist.
        """
        reservation = await Reservation.load_from_db(db, confirmation_number)
        if reservation:
            return f"Name: {self.name}, 
                    Dates: {reservation.get_dates()}, 
                    Room Type: {'Suite' if reservation.room_id < 200 else 'Double' if reservation.room_id < 300 else 'Single'}, 
                    Confirmation Number: {reservation.get_confirmation_number()}"
        return "Not Found"

    async def check_reservation(self, confirmation_number: int, db):
        """
            Checks if a reservation exists and returns a formatted string with reservation details.

            Args:
                confirmation_number (int): The confirmation number of the reservation.
                db: The database connection object.

            Returns:
                str: A formatted string with reservation details if found, otherwise 'Not Found'.
        """
        
        reservation = await Reservation.load_from_db(db, confirmation_number)
        if reservation:
            return f"Reservation Found: Name: {self.name}, Room ID: {reservation.room_id}, Dates: {reservation.get_dates()}"
        return "Not Found"
        