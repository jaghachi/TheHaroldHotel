"""""
main window -> booking window -> booking room window -> room booking details
the window shows all the details of the booking chose by the user: room type, number of guests, the dates. The window prompts user to enter their name and email.
"""""

"""""
class: RoomBookingDetailsWindow
most recent update: 8/12/2024

programmers: Mariia Kim

Description:
The RoomBookingDetailsWindow class is the final step in the booking process, 
opened from the BookingRoomsWindow. It allows the user to review the selected room details, 
enter their name and email for the booking, and confirm the reservation.
"""""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSpacerItem, QSizePolicy, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from classes.reservation import Reservation
from classes.customer import Customer
from views.Page_5_BookingConfirmationWindow import BookingConfirmationWindow
import asyncio
import pydoc

class RoomBookingDetailsWindow(QWidget):
    """""
    This window provides the interface for users to input their personal information before finalizing 
    their booking. It also handles the transition to the booking confirmation window upon successful booking.

    Attributes:
        controller (ViewController): Manages view transitions and interactions with other views.
        name_input (QLineEdit): Input field for the user's name.
        email_input (QLineEdit): Input field for the user's email.

    Methods:
        handle_booking(user_name, user_email, adults, room, newReservation): Asynchronously processes the booking details and transitions to the booking confirmation window.
        open_booking_confirmation(newReservation): Opens the BookingConfirmationWindow to display the booking confirmation.
        back_to_booking_rooms(): Navigates back to the BookingRoomsWindow.
    """""
    def __init__(self, room, newReservation, adults, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle(f"{room['name']} Booking")
        self.setGeometry(100, 100, 800, 600)
        
        # set up the background pic
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("resources/lobby.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 800, 600)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0) # no margins
        main_layout.setSpacing(0) # no spacing between widgets
        self.setLayout(main_layout)

        # spacer item to push the centered_frame to the middle
        spacer_top = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        # centered container for the date and guest selection widgets
        centered_frame = QFrame(self)
        centered_frame.setStyleSheet("background-color: #E5D5C3; border-radius: 10px;")
        centered_frame.setFixedSize(500, 300)
        centered_layout = QVBoxLayout(centered_frame)

        # creating a label for the name of the room
        room_name = QLabel(room["name"])
        room_name.setStyleSheet("font-size: 15px; color: black; font-weight: bold;")
        room_name.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(room_name)

        details_label = QLabel(f"Booking for {adults} people\nCheck-in: {newReservation.checkIn.toString('MMM d, yyyy')} - Check-out: {newReservation.checkOut.toString('MMM d, yyyy')}")
        details_label.setStyleSheet("font-size: 18px; color: black;")
        details_label.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(details_label)

        name_label = QLabel("Enter the name for the booking: ")
        name_label.setStyleSheet("font-size: 18px; color: black;")
        name_label.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(name_label)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Your Name")
        self.name_input.setStyleSheet("border: 1px solid #000000;")
        centered_layout.addWidget(self.name_input)

        email_label = QLabel("Enter the email for the booking: ")
        email_label.setStyleSheet("font-size: 18px; color: black;")
        email_label.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(email_label)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Your email")
        self.email_input.setStyleSheet("border: 1px solid #000000;")
        centered_layout.addWidget(self.email_input)

        book_button = QPushButton("Book")
        book_button.setStyleSheet("""
            QPushButton {
                background-color: #E5D5C3;
                color: black;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2B1C19;
                color: white;
            }
        """)
        book_button.clicked.connect(lambda: asyncio.ensure_future(
            self.handle_booking(
                self.name_input.text(),
                self.email_input.text(),
                adults,
                room, 
                newReservation
            )
        ))
        centered_layout.addWidget(book_button)

        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #E5D5C3;
                color: black;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2B1C19;
                color: white;
            }
        """)
        back_button.clicked.connect(self.back_to_booking_rooms)
        centered_layout.addWidget(back_button)
        # adding the centered frame to the main layout
        center_container = QHBoxLayout()
        center_container.addStretch()
        center_container.addWidget(centered_frame)
        center_container.addStretch()
        main_layout.addLayout(center_container)

        # spacer item to push the centered_frame to the middle
        spacer_bottom = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_bottom)

        self.setLayout(main_layout)

    async def handle_booking(self, user_name, user_email, adults, room, newReservation):
        new_customer = Customer()
        new_customer.set_name(user_name)
        new_customer.set_email(user_email)
        new_customer.set_persons(adults)
        await newReservation.reserveRoom(room, new_customer, newReservation)
        self.open_booking_confirmation(newReservation)

    def open_booking_confirmation(self, newReservation):
        self.confirmation_window = BookingConfirmationWindow(newReservation,self.controller)
        self.confirmation_window.setWindowModality(Qt.ApplicationModal)
        self.controller.add_view(self.confirmation_window, "confirmation")
        self.controller.show_view("confirmation")
        
    def back_to_booking_rooms(self):
        self.controller.show_view("booking_rooms")
