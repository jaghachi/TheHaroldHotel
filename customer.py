class Customer:
    def __init__(self, name: str, email: str, persons: int, reservations: list):
        self.name = name
        self.email = email
        self.persons = persons
        self.reservations = reservations

    def getEmail(self) -> str:
        return self.email

    def getPersons(self) -> int:
        return self.persons

    def getReservations(self) -> list:
        return self.reservations

    def setEmail(self, email: str):
        self.email = email

    def setPersons(self, persons: int):
        self.persons = persons

    def setName(self, name: str):
        self.name = name

    def setReservation(self, reservations: list):
        self.reservations = reservations
        