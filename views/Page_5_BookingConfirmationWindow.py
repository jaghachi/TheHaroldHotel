from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class BookingConfirmationWindow(QWidget):
    def __init__(self, booked, controller):
        super().__init__()
        self.controller = controller  # Added controller
        self.setWindowTitle("Booking Confirmation")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet("background-color: #E5D5C3")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        confirmation_label = QLabel("Your booking is confirmed!")
        confirmation_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2B1C19;")
        confirmation_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(confirmation_label)

        details_label = QLabel(f"Room: {booked.roomName}\nCheck-in: {booked.checkIn.toString('MMM d, yyyy')} - Check-out: {booked.checkOut.toString('MMM d, yyyy')}\nGuests: {booked.persons}")
        details_label.setStyleSheet("font-size: 18px; color: black;")
        details_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(details_label)

        user_name_label = QLabel(f"Name: {booked.customer.get_name()}")
        user_name_label.setStyleSheet("font-size: 18px; color: black;")
        user_name_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(user_name_label)

        confirmation_number_label = QLabel(f"Confirmation #: {booked.confirmationNumber}")
        confirmation_number_label.setStyleSheet("font-size: 18px; font-weight: bold; color: black;")
        confirmation_number_label.setAlignment(Qt.AlignCenter)
        confirmation_number_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        main_layout.addWidget(confirmation_number_label)

        closing_message = QLabel(f"See you soon, {booked.customer.get_name()}!")
        closing_message.setStyleSheet("font-size: 20px; color: #2B1C19;")
        closing_message.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(closing_message)

        done_button = QPushButton("Done")
        done_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        done_button.clicked.connect(self.back_to_main)
        main_layout.addWidget(done_button)

    def back_to_main(self):
        self.controller.show_view("main")
