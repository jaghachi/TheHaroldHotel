class Customer:
    
    # Customer class with reservations

    def __init__(self):
        # Initialize an empty Customer
        self.name = ""
        self.email = ""
        self.persons = 0
        self.reservations = []

    # Getter and Setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and Setter for email
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    # Getter and Setter for persons
    def get_persons(self):
        return self.persons

    def set_persons(self, persons):
        self.persons = persons

    # Getter and Setter for reservations
    def get_reservations(self):
        return self.reservations

    def add_reservation(self, reservation):
        # Add a reservation to the list
        self.reservations.append(reservation)