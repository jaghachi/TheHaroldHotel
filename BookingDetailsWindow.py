
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

# displaying the booking based on the confirmation #
class BookingDetailsWindow(QWidget):
    def __init__(self, booking_info):
        super().__init__()
        self.setWindowTitle("Booking Details")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #E5D5C3;")

        main_layout = QVBoxLayout()

        # Display booking information as in bookingConfirmationWindow
        title = QLabel(f"Booking Confirmation for {booking_info['name']}")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2B1C19;")
        main_layout.addWidget(title)

        room_details = QLabel(f"Room Type: {booking_info['room_type']}\n"
            f"Check-in: {booking_info['checkin_date'].toString('MMM d, yyyy')}\n"
            f"Check-out: {booking_info['checkout_date'].toString('MMM d, yyyy')}\n"
            f"Guests: {booking_info['guests']}\n"
            f"Confirmation Number: {booking_info['confirmation_number']}")
        room_details.setAlignment(Qt.AlignCenter)
        room_details.setStyleSheet("font-size: 16px; color: black;")
        main_layout.addWidget(room_details)

        # Buttons for change reservation
        change_button = QPushButton("Change Reservation")
        change_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        # connect it to open a new window
        change_button.clicked.connect(self.change_reservation)
        main_layout.addWidget(change_button)

        # button for cancel reservation
        cancel_button = QPushButton("Cancel Reservation")
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        # connect it to open a new window
        cancel_button.clicked.connect(self.cancel_reservation)
        main_layout.addWidget(cancel_button)
        # a button for returning
        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        # connect the button to return back
        back_button.clicked.connect(self.close)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

    def change_reservation(self):
        # Implement logic to change the reservation
        QMessageBox.information(self, "Change Reservation", "Reservation change functionality is not implemented yet.")

    def cancel_reservation(self):
        # Implement logic to cancel the reservation
        QMessageBox.information(self, "Cancel Reservation", "Reservation cancellation functionality is not implemented yet.")