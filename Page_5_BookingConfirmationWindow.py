from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import random
import string

# Window that opens after you press book in the room selection
class BookingConfirmationWindow(QWidget):
    def __init__(self, room_name, checkin_date, checkout_date, guests, user_name):
        super().__init__()
        self.setWindowTitle("Booking Confirmation")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet("background-color: #E5D5C3")

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Confirmation message
        confirmation_label = QLabel("Your booking is confirmed!")
        confirmation_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2B1C19;")
        confirmation_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(confirmation_label)

        # Booking details
        details_label = QLabel(f"Room: {room_name}\nCheck-in: {checkin_date.toString('MMM d, yyyy')} - Check-out: {checkout_date.toString('MMM d, yyyy')}\nGuests: {guests}")
        details_label.setStyleSheet("font-size: 18px; color: black;")
        details_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(details_label)

        # User name
        user_name_label = QLabel(f"Name: {user_name}")
        user_name_label.setStyleSheet("font-size: 18px; color: black;")
        user_name_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(user_name_label)

        # Generate a confirmation number
        confirmation_number = self.generate_confirmation_number()
        confirmation_number_label = QLabel(f"Confirmation #: {confirmation_number}")
        confirmation_number_label.setStyleSheet("font-size: 18px; font-weight: bold; color: black;")
        confirmation_number_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(confirmation_number_label)

        # Closing message
        closing_message = QLabel(f"See you soon, {user_name}!")
        closing_message.setStyleSheet("font-size: 20px; color: #2B1C19;")
        closing_message.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(closing_message)

    def generate_confirmation_number(self):
        return ''.join(random.choices(string.digits, k=10))
