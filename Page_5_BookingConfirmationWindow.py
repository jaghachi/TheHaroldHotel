from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import random
import string

# Window that opens after you press book in the room selection
class BookingConfirmationWindow(QWidget):
    def __init__(self, booked):
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
        details_label = QLabel(f"Room: {booked.roomName}\nCheck-in: {booked.checkin_date.toString('MMM d, yyyy')} - Check-out: {booked.checkout_date.toString('MMM d, yyyy')}\nGuests: {booked.persons}")
        details_label.setStyleSheet("font-size: 18px; color: black;")
        details_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(details_label)

        # User name
        user_name_label = QLabel(f"Name: {booked.customer.name}")
        user_name_label.setStyleSheet("font-size: 18px; color: black;")
        user_name_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(user_name_label)

        # Generate a confirmation number
        confirmation_number_label = QLabel(f"Confirmation #: {booked.confirmationNumber}")
        confirmation_number_label.setStyleSheet("font-size: 18px; font-weight: bold; color: black;")
        confirmation_number_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(confirmation_number_label)

        # Closing message
        closing_message = QLabel(f"See you soon, {booked.customer.name}!")
        closing_message.setStyleSheet("font-size: 20px; color: #2B1C19;")
        closing_message.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(closing_message)

    def generate_confirmation_number(self):
        return ''.join(random.choices(string.digits, k=10))
