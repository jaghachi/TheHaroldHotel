class Customer:
    
    # Customer class with reservations

    def __init__(self):
        # Initialize an empty Customer
        self.name = None
        self.email = None
        self.persons = None
        self.reservations = []

    # Getter and Setter for name
    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    # Getter and Setter for email
    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    # Getter and Setter for persons
    def get_persons(self):
        return self.persons

    def set_persons(self, value):
        self.persons = value

    # Getter and Setter for reservations
    def get_reservations(self):
        return self.reservations

    def add_reservation(self, reservation):
        # Add a reservation to the list
        self.reservations.append(reservation)