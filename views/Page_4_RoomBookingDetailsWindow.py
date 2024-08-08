# roombookingdetailswindow.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from classes.reservation import Reservation
from classes.customer import Customer
from views.Page_5_BookingConfirmationWindow import BookingConfirmationWindow
import asyncio

class RoomBookingDetailsWindow(QWidget):
    def __init__(self, room, newReservation, adults, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle(f"{room['name']} Booking")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet("background-color: #E5D5C3")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        room_image_label = QLabel()
        pixmap = QPixmap(room["image"]).scaled(300, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        room_image_label.setPixmap(pixmap)
        room_image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(room_image_label)

        room_name = QLabel(room["name"])
        room_name.setStyleSheet("font-size: 15px; color: black; font-weight: bold;")
        room_name.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(room_name)

        details_label = QLabel(f"Booking for {adults} people\nCheck-in: {newReservation.checkIn.toString('MMM d, yyyy')} - Check-out: {newReservation.checkOut.toString('MMM d, yyyy')}")
        details_label.setStyleSheet("font-size: 18px; color: black;")
        details_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(details_label)

        name_label = QLabel("Enter the name for the booking: ")
        name_label.setStyleSheet("font-size: 18px; color: black;")
        name_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(name_label)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Your Name")
        main_layout.addWidget(self.name_input)

        email_label = QLabel("Enter the email for the booking: ")
        email_label.setStyleSheet("font-size: 18px; color: black;")
        email_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(email_label)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Your email")
        main_layout.addWidget(self.email_input)

        buttons_layout = QHBoxLayout()

        book_button = QPushButton("Book")
        book_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
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
        buttons_layout.addWidget(book_button)

        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        back_button.clicked.connect(self.back_to_booking_rooms)
        buttons_layout.addWidget(back_button)

        main_layout.addLayout(buttons_layout)

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
