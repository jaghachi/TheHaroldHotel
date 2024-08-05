from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

# check booking -> input confirmation # -> it exists
class BookingDetailsWindow(QWidget):
    def __init__(self, confirmation_number):
        super().__init__()
        self.setWindowTitle("Booking Details")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #765A45;")

        main_layout = QVBoxLayout()

        # Placeholder booking details
        booking_details = f"Booking Details for Confirmation Number: {confirmation_number}\n\n"
        booking_details += "Name: John Doe\n"
        booking_details += "Check-in Date: 2024-08-10\n"
        booking_details += "Check-out Date: 2024-08-15\n"
        booking_details += "Room Type: Deluxe Suite\n"
        booking_details += "Total Price: $1500\n"

        booking_label = QLabel(booking_details)
        booking_label.setAlignment(Qt.AlignTop)
        booking_label.setStyleSheet("font-size: 14px; color: white;")
        main_layout.addWidget(booking_label)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
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
        close_button.clicked.connect(self.close)
        main_layout.addWidget(close_button)

        self.setLayout(main_layout)
