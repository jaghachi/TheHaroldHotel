# main window -> booking window -> booking rooms window -> room booking details window -> confirmation
""""
class: BookingConfirmationWindow
most recent update: 8/12/2024

programmers: Mariia Kim, Harold Flint

Description:
The BookingConfirmationWindow class is the final step in the booking process, opened from the RoomBookingDetailsWindow. 
It displays the confirmation details of the booking, including room information, check-in/check-out dates, 
number of guests, and the customer's name.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout,QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import pydoc

class BookingConfirmationWindow(QWidget):
    """"
    This window provides a summary of the completed booking and gives the user a confirmation number, 
    along with a personalized message. The user can click "Done" to return to the main window.

    Attributes:
        controller (ViewController): Manages view transitions and interactions with other views.

    Methods:
        back_to_main(): Navigates back to the MainWindow after the booking is confirmed.
    """
    def __init__(self, booked, controller):
        super().__init__()
        self.controller = controller  # Added controller
        self.setWindowTitle("Booking Confirmation")
        self.setGeometry(100, 100, 800, 600)
        
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
        centered_frame.setFixedSize(500, 300)
        centered_layout = QVBoxLayout(centered_frame)

        confirmation_label = QLabel("Your booking is confirmed!")
        confirmation_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2B1C19;")
        confirmation_label.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(confirmation_label)

        details_label = QLabel(f"Room: {booked.roomName}\nCheck-in: {booked.checkIn.toString('MMM d, yyyy')} - Check-out: {booked.checkOut.toString('MMM d, yyyy')}\nGuests: {booked.persons}")
        details_label.setStyleSheet("font-size: 18px; color: black;")
        details_label.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(details_label)

        user_name_label = QLabel(f"Name: {booked.customer.get_name()}")
        user_name_label.setStyleSheet("font-size: 18px; color: black;")
        user_name_label.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(user_name_label)

        confirmation_number_label = QLabel(f"Confirmation #: {booked.confirmationNumber}")
        confirmation_number_label.setStyleSheet("font-size: 18px; font-weight: bold; color: black;")
        confirmation_number_label.setAlignment(Qt.AlignCenter)
        confirmation_number_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        centered_layout.addWidget(confirmation_number_label)

        closing_message = QLabel(f"See you soon, {booked.customer.get_name()}!")
        closing_message.setStyleSheet("font-size: 20px; color: #2B1C19;")
        closing_message.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(closing_message)

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
        centered_layout.addWidget(done_button)

        center_container = QHBoxLayout()
        center_container.addStretch()
        center_container.addWidget(centered_frame)
        center_container.addStretch()
        main_layout.addLayout(center_container)

        spacer_bottom = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_bottom)

    def back_to_main(self):
        self.controller.show_view("main")
