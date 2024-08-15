"""
class: Customer
most recent update: 8/12/2024

programmers: Jonathan Aghachi and Macy V

Description:
"Customer" class represents a customer with a name, email, number of persons, and a list of reservations. 
"""
import pydoc
class Customer:
    """
    A class to represent a customer with associated reservations.

    Attributes:
    -----------
    name : str
        The name of the customer.
    email : str
        The email address of the customer.
    persons : int
        The number of persons included in the customer's reservation.
    reservations : list
        A list to store the customer's reservations.

    Methods:
    --------
    get_name() -> str:
        Returns the name of the customer.
    set_name(name: str) -> None:
        Sets the name of the customer.
    get_email() -> str:
        Returns the email address of the customer.
    set_email(email: str) -> None:
        Sets the email address of the customer.
    get_persons() -> int:
        Returns the number of persons associated with the customer's reservation.
    set_persons(persons: int) -> None:
        Sets the number of persons associated with the customer's reservation.
    get_reservations() -> list:
        Returns the list of reservations for the customer.
    add_reservation(reservation: object) -> None:
        Adds a reservation to the customer's list of reservations.
    """

    # Customer class with reservations

    def __init__(self):
        """
        Initializes an empty Customer with default values for name, email, persons, and an empty list of reservations.
        """
        # Initialize an empty Customer
        self.name = ""
        self.email = ""
        self.persons = 0
        self.reservations = []

    # Getter and Setter for name
    def get_name(self):
        """
        Returns the name of the customer.

        Returns:
        --------
        str
            The name of the customer.
        """
        return self.name

    def set_name(self, name):
        """
        Sets the name of the customer.

        Parameters:
        -----------
        name : str
            The new name to be assigned to the customer.
        """
        self.name = name

   # Getter and Setter for email
    def get_email(self):
        """
        Returns the email address of the customer.

        Returns:
        --------
        str
            The email address of the customer.
        """
        return self.email

    def set_email(self, email):
        """
        Sets the email address of the customer.

        Parameters:
        -----------
        email : str
            The new email address to be assigned to the customer.
        """
        self.email = email

    # Getter and Setter for persons
    def get_persons(self):
        """
        Returns the number of persons associated with the customer's reservation.

        Returns:
        --------
        int
            The number of persons in the reservation.
        """
        return self.persons

    def set_persons(self, persons):
        """
        Sets the number of persons associated with the customer's reservation.

        Parameters:
        -----------
        persons : int
            The number of persons to be associated with the reservation.
        """
        self.persons = persons

    # Getter and Setter for reservations
    def get_reservations(self):
        """
        Returns the list of reservations for the customer.

        Returns:
        --------
        list
            The list of the customer's reservations.
        """
        return self.reservations

    def add_reservation(self, reservation):

        """
        Adds a reservation to the customer's list of reservations.

        Parameters:
        -----------
        reservation : object
            The reservation to be added to the list.
        """
        # Add a reservation to the list
        self.reservations.append(reservation)