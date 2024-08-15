"""""
main window -> check booking -> booking details window
lets the user see all their booking details (existing booking)
"""""
"""
class: BookingDetailsWindow
most recent update: 8/12/2024

programmers: Mariia Kim

Description: aloows user to view the details of an existing booking, such as check-in and check-out dates, room type, and total price.
    provides options for the user to change or cancel the booking
"""
from datetime import datetime, time
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QHBoxLayout, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from views.CancelBookingDialog import CancelBookingDialog
from views.ChangeBookingWindow import ChangeBookingWindow
import asyncio
import pydoc

class BookingDetailsWindow(QWidget):
    """
    A window to display the details of a user's existing booking.

    This window is part of a sequence of views:
    Main Window -> Check Booking -> Booking Details Window

    Attributes:
    -----------
    reservation : dict
        A dictionary containing the details of the reservation.
    customer : dict
        A dictionary containing the customer's information.
    room : dict
        A dictionary containing information about the room booked.
    roomType : dict
        A dictionary containing the type of room booked and its price.
    controller : object
        The controller object to manage the application's views and transitions.
    """
    def __init__(self, reservation, customer, room, roomType, controller):
        """
        Initializes the BookingDetailsWindow with the provided reservation details,
        customer information, room, and room type.

        Parameters:
        -----------
        reservation : dict
            The reservation details to be displayed.
        customer : dict
            The customer's information to be displayed.
        room : dict
            The room details for the booking.
        roomType : dict
            The type of room booked, including its price.
        controller : object
            The controller managing the views and transitions.
        """
        super().__init__()
        self.controller = controller  # added controller
        self.reservation = reservation
        self.customer = customer
        self.room = room
        self.roomType = roomType
        self.setWindowTitle("Booking Details")
        self.setGeometry(100, 100, 800, 600)
        
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("resources/lobby.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 800, 600)

        main_layout = QVBoxLayout()

        spacer_top = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        centered_frame = QFrame(self)
        centered_frame.setStyleSheet("background-color: #E5D5C3; border-radius: 10px;")
        centered_frame.setFixedSize(500, 250)

        centered_layout = QVBoxLayout(centered_frame)
        
        checkIn_time = time(15, 0)
        checkOut_time = time(13, 0)
        
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

        change_booking_button = QPushButton("Change Booking")
        change_booking_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)

        change_booking_button.clicked.connect(lambda: asyncio.ensure_future(
            self.change_booking()))
        
        
        
        centered_layout.addWidget(change_booking_button)

        cancel_booking_button = QPushButton("Cancel Booking")
        cancel_booking_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        cancel_booking_button.clicked.connect(self.cancel_booking)
        centered_layout.addWidget(cancel_booking_button)

        center_container = QHBoxLayout()
        center_container.addStretch()
        center_container.addWidget(centered_frame)
        center_container.addStretch()
        main_layout.addLayout(center_container)

        spacer_bottom = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_bottom)

        self.setLayout(main_layout)

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
        back_button.clicked.connect(self.back_to_main)
        bottom_layout.addWidget(back_button)
        main_layout.addStretch()

        main_layout.addLayout(bottom_layout)

    def back_to_main(self):
        """Returns to the main window view."""
        self.controller.show_view("main")

    async def change_booking(self):
        """
        Opens a window to change the booking details.

        Creates a new instance of ChangeBookingWindow and transitions to it.
        """
        change_booking_window = ChangeBookingWindow(self.reservation, self.customer, self.roomType, self.controller)
        self.controller.add_view(change_booking_window, "change_booking")
        self.controller.show_view("change_booking")

    def cancel_booking(self):
        """
        Opens a dialog to cancel the booking.

        Displays a CancelBookingDialog to confirm the cancellation of the booking.
        """
        dialog = CancelBookingDialog(self, self.controller)
        dialog.exec_()