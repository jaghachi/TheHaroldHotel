# main window -> check booking window
"""
class: CheckBookingWindow
most recent update: 8/12/2024

programmers: Mariia Kim, Harold Flint

Description:
The CheckBookingWindow class allows users to check the details of their reservation by entering a confirmation number. 
It is opened from the MainWindow and provides an interface for users to input their confirmation number 
and retrieve their booking details.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QFrame, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from views.BookingDetailsWindow import BookingDetailsWindow
from databaseFiles.databaseconnect import dataBase
import asyncio
import pydoc

class CheckBookingWindow(QWidget):
    """
    If the confirmation number is valid, the user is redirected to the BookingDetailsWindow, 
    where they can view the specifics of their reservation. The class also handles error messages 
    if the confirmation number is not found.

    Attributes:
        controller (ViewController): Manages view transitions and interactions with other views.
        confirmation_input (QLineEdit): Input field for the user to enter their confirmation number.
        error_label (QLabel): Label for displaying error messages when the confirmation number is not found.

    Methods:
        check_booking(): Asynchronously checks the database for the entered confirmation number and transitions to the BookingDetailsWindow if found.
        back_to_main(): Navigates back to the MainWindow.
    """
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # added controller
        self.setWindowTitle("Check your reservation")
        self.setGeometry(100, 100, 800, 600)

        # set up the background pic
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("resources/lobby.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 800, 600)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)  
        main_layout.setSpacing(0)  
        self.setLayout(main_layout)

        spacer_top = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        centered_frame = QFrame(self)
        centered_frame.setStyleSheet("background-color: #E5D5C3; border-radius: 10px;")
        centered_frame.setFixedSize(400, 150)

        centered_layout = QVBoxLayout(centered_frame)

        title = QLabel("Input your Confirmation Number: ")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; color: black;")
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
