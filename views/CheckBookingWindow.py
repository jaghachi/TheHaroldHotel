"""""
main window -> check booking window
the window allows the user to input their booking confirmation number to check their booking. The window will display an error message if the booking doesn't exist. 
If the confirmation number exists, then the user will be brought to the next frame.
"""""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QFrame, QHBoxLayout
from PyQt5.QtGui import QPixmap
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

        # set up the background pic
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("resources/lobby.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 800, 600)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)  # No margins
        main_layout.setSpacing(0)  # No spacing between widgets
        self.setLayout(main_layout)

        # spacer item to push the centered_frame to the middle
        spacer_top = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        # centered frame
        centered_frame = QFrame(self)
        centered_frame.setStyleSheet("background-color: #E5D5C3; border-radius: 10px;")
        centered_frame.setFixedSize(400, 150)

        centered_layout = QVBoxLayout(centered_frame)

        title = QLabel("Input your Confirmation Number: ")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; color: white;")
        centered_layout.addWidget(title)

        self.confirmation_input = QLineEdit(self)
        self.confirmation_input.setStyleSheet("background-color: white; color: black; padding: 5px;")
        centered_layout.addWidget(self.confirmation_input)

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
        centered_layout.addWidget(check_button)

        self.error_label = QLabel("")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setStyleSheet("font-size: 10px; color: red;")
        centered_layout.addWidget(self.error_label)

        # adding the centered frame to the main layout
        center_container = QHBoxLayout()
        center_container.addStretch()
        center_container.addWidget(centered_frame)
        center_container.addStretch()
        main_layout.addLayout(center_container)

        # spacer item to push the centered_frame to the middle
        spacer_bottom = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_bottom)
        
        # add the back button to the bottom right corner
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()

        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        # back button brings the user to the previous frame
        back_button.clicked.connect(self.back_to_main)
        bottom_layout.addWidget(back_button)
        main_layout.addLayout(bottom_layout)

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
