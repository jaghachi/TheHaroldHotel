"""""
main window -> check booking -> booking details window
lets the user see all their booking details (existing booking)
"""""
from datetime import datetime, time
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class BookingDetailsWindow(QWidget):
    def __init__(self, reservation, customer, room, roomType, controller):
        super().__init__()
        self.controller = controller  # Added controller
        self.setWindowTitle("Booking Details")
        self.setGeometry(100, 100, 800, 600)
        
        # set up the background pic
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("resources/lobby.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 800, 600)

        main_layout = QVBoxLayout()

        # spacer item to push the centered_frame to the middle
        spacer_top = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        # centered frame to hold the booking details and buttons
        centered_frame = QFrame(self)
        centered_frame.setStyleSheet("background-color: #E5D5C3; border-radius: 10px;")
        centered_frame.setFixedSize(500, 250)

        centered_layout = QVBoxLayout(centered_frame)
        
        checkIn_time = time(15, 0)
        checkOut_time = time(13, 0)
        
        # Convert ISODate strings to datetime objects and adjust time
        checkIn = datetime.fromisoformat(str(reservation['checkIn'])).replace(hour=checkIn_time.hour, minute=checkIn_time.minute)
        checkOut = datetime.fromisoformat(str(reservation['checkOut'])).replace(hour=checkOut_time.hour, minute=checkOut_time.minute)

        # Calculate nights
        nights = (checkOut.replace(hour=0, minute=0, second=0, microsecond=0) - checkIn.replace(hour=0, minute=0, second=0, microsecond=0)).days

        # Placeholder booking details
        booking_details = f"Booking Details for Confirmation Number: {reservation['confirmationNumber']}\n\n"
        booking_details += f"Name: {customer['name']}\n"
        booking_details += f"Check-in Date: {checkIn.strftime('%b %d %Y') + ' at ' + checkIn.strftime('%I:%M%p').lower()}\n"
        booking_details += f"Check-out Date: {checkOut.strftime('%b %d %Y') + ' at ' + checkOut.strftime('%I:%M%p').lower()}\n"
        booking_details += f"Room Type: {roomType['type']}\n"
        booking_details += f"Total Price: ${nights * roomType['price']}\n"  # should change to save calculation at reservation stage

        booking_label = QLabel(booking_details)
        booking_label.setAlignment(Qt.AlignTop)
        booking_label.setStyleSheet("font-size: 14px; color: black;")
        centered_layout.addWidget(booking_label)

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
        back_button.clicked.connect(self.back_to_main)
        centered_layout.addWidget(back_button)

        # add the centered frame to the main layout
        center_container = QHBoxLayout()
        center_container.addStretch()
        center_container.addWidget(centered_frame)
        center_container.addStretch()
        main_layout.addLayout(center_container)

        # spacer item AGAIN to push the centered_frame to the middle
        spacer_bottom = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_bottom)

        self.setLayout(main_layout)

    def back_to_main(self):
        self.controller.show_view("main")
