from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from views.BookingDetailsWindow import BookingDetailsWindow
from databaseFiles.databaseconnect import dataBase
import asyncio

class CheckBookingWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # Added controller
        self.setWindowTitle("Check your reservation")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #765A45;")

        main_layout = QVBoxLayout()

        title = QLabel("Input your Confirmation Number: ")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; color: white;")
        main_layout.addWidget(title)

        self.confirmation_input = QLineEdit(self)
        self.confirmation_input.setStyleSheet("background-color: white; color: black; padding: 5px;")
        main_layout.addWidget(self.confirmation_input)

        check_button = QPushButton("Check Booking")
        check_button.setStyleSheet("""
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
        check_button.clicked.connect(lambda: asyncio.ensure_future(self.check_booking()))
        main_layout.addWidget(check_button)

        self.error_label = QLabel("")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setStyleSheet("font-size: 10px; color: red;")
        main_layout.addWidget(self.error_label)

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
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

    async def check_booking(self):
        confirmation_number = self.confirmation_input.text().strip()
        print(f"Checking booking for confirmation number: {confirmation_number}")

        db_instance = dataBase()
        db = await db_instance.get_database()
        reservations = db['reservations']
        customers = db['customers']
        rooms = db['rooms']
        roomTypes = db['roomTypes']

        reservation = await reservations.find_one({"confirmationNumber": confirmation_number})

        if not reservation:
            self.error_label.setText("Confirmation number not found. Please try again.")
        else:
            customer = await customers.find_one({"_id": reservation['customerId']})
            room = await rooms.find_one({"_id": reservation['roomId']})
            roomType = await roomTypes.find_one({"_id": room['typeId']})
            self.booking_details_window = BookingDetailsWindow(reservation, customer, room, roomType, self.controller)  # Added controller
            self.controller.add_view(self.booking_details_window, "booking_details")  # Added controller
            self.controller.show_view("booking_details")  # Added controller

    def back_to_main(self):
        self.controller.show_view("main")
