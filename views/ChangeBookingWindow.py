# main window -> check booking -> change booking
"""
class: ChangeBookingWindow
most recent update: 8/13/2024

programmers: Mariia Kim

Description:
The ChangeBookingWindow class allows users to modify their existing booking details. 
This window is opened from the CheckBookingWindow and provides an interface for users 
to change their room type, check-in and check-out dates, and the number of guests. 
This window is opened from the CheckBookingWindow and provides an interface for users 
to change their room type, check-in and check-out dates, and the number of guests.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDateEdit, QComboBox, QPushButton, QFrame, QHBoxLayout, QSizePolicy, QSpacerItem, QMessageBox
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap
from databaseFiles.databaseconnect import dataBase
import asyncio

import pydoc

class ChangeBookingWindow(QWidget):
    """
    Once the user submits their changes, the updates are processed and the user is returned 
    to the booking details view with a confirmation message indicating that the changes were successfully submitted.

    Attributes:
        controller (ViewController): Manages view transitions and interactions with other views.
        reservation (dict): Contains the current reservation details.
        customer (dict): Contains the customer's information.
        roomType (dict): Contains the current room type information.
        room_type_combo (QComboBox): Drop-down list for selecting the new room type.
        checkin_date (QDateEdit): Widget for selecting the new check-in date.
        checkout_date (QDateEdit): Widget for selecting the new check-out date.
        guests_combo (QComboBox): Drop-down list for selecting the new number of guests.

    Methods:
        back_to_booking_details(): Navigates back to the BookingDetailsWindow.
        submit_changes(): Handles the submission of the updated booking details and shows a confirmation dialog.
        show_confirmation_dialog(): Displays a confirmation message indicating that the booking changes were successfully submitted.
    """
    def __init__(self, reservation, customer, roomType, controller):
        super().__init__()
        self.controller = controller
        self.reservation = reservation
        self.customer = customer
        self.roomType = roomType

        self.setWindowTitle("Change Booking")
        self.setGeometry(100, 100, 800, 600)

        # Set up the background pic (optional)
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("resources/lobby.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 800, 600)

        main_layout = QVBoxLayout()

        # Spacer item to push the centered_frame to the middle
        spacer_top = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        # Centered frame to hold the change booking form
        centered_frame = QFrame(self)
        centered_frame.setStyleSheet("background-color: #E5D5C3; border-radius: 10px;")
        centered_frame.setFixedSize(500, 400)

        centered_layout = QVBoxLayout(centered_frame)

        title = QLabel("Change Your Booking")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        centered_layout.addWidget(title)

        name_label = QLabel(f"Name: {self.customer['name']}")
        name_label.setStyleSheet("color: black;")
        name_label.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(name_label)

        email_label = QLabel(f"Email: {self.customer['email']}")
        email_label.setStyleSheet("color: black;")
        email_label.setAlignment(Qt.AlignCenter)
        centered_layout.addWidget(email_label)

        # Room Type Selection
        room_type_layout = QVBoxLayout()
        room_type_label = QLabel("New Room Type")
        room_type_label.setStyleSheet("color: black;")
        room_type_label.setAlignment(Qt.AlignCenter)
        self.room_type_combo = QComboBox()
        self.room_type_combo.addItems(["Premiere Harold Single", "Premiere Harold Double", "Premiere Harold Suite"])  
        self.room_type_combo.setCurrentText(self.roomType['type'])
        self.room_type_combo.setStyleSheet("""
            QComboBox {
                color: black;
                background-color: white;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QComboBox QAbstractItemView {
                color: black;
                background-color: white;
                selection-background-color: #E5D5C3;
            }
        """)
        room_type_layout.addWidget(room_type_label)
        room_type_layout.addWidget(self.room_type_combo)
        centered_layout.addLayout(room_type_layout)

        checkin_layout = QVBoxLayout()
        checkin_label = QLabel("New Check-in Date")
        checkin_label.setStyleSheet("color: black;")
        checkin_label.setAlignment(Qt.AlignCenter)
        self.checkin_date = QDateEdit()
        self.checkin_date.setDate(QDate(self.reservation['checkIn'].year, self.reservation['checkIn'].month, self.reservation['checkIn'].day))
        self.checkin_date.setCalendarPopup(True)
        checkin_layout.addWidget(checkin_label)
        checkin_layout.addWidget(self.checkin_date)
        centered_layout.addLayout(checkin_layout)

        checkout_layout = QVBoxLayout()
        checkout_label = QLabel("New Check-out Date")
        checkout_label.setStyleSheet("color: black;")
        checkout_label.setAlignment(Qt.AlignCenter)
        self.checkout_date = QDateEdit()
        self.checkout_date.setDate(QDate(self.reservation['checkOut'].year, self.reservation['checkOut'].month, self.reservation['checkOut'].day))
        self.checkout_date.setCalendarPopup(True)
        checkout_layout.addWidget(checkout_label)
        checkout_layout.addWidget(self.checkout_date)
        centered_layout.addLayout(checkout_layout)

        guests_layout = QVBoxLayout()
        guests_label = QLabel("Guests")
        guests_label.setStyleSheet("color: black;")
        guests_label.setAlignment(Qt.AlignCenter)
        self.guests_combo = QComboBox()
        self.guests_combo.addItems([str(i) for i in range(1, 6)])
        self.guests_combo.setCurrentText(str(self.reservation.get('guests', 1)))  # Set the current number of guests or default to 1
        self.guests_combo.setStyleSheet("""
            QComboBox {
                color: black;
                background-color: white;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QComboBox QAbstractItemView {
                color: black;
                background-color: white;
                selection-background-color: #E5D5C3;
            }
        """)
        guests_layout.addWidget(guests_label)
        guests_layout.addWidget(self.guests_combo)
        centered_layout.addLayout(guests_layout)

        submit_button = QPushButton("Submit Changes")
        submit_button.setStyleSheet("""
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
        submit_button.clicked.connect(lambda: asyncio.ensure_future(
            self.submit_changes()))
        
        
        centered_layout.addWidget(submit_button)

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
        back_button.clicked.connect(self.back_to_booking_details)
        bottom_layout.addWidget(back_button)
        main_layout.addStretch()

        main_layout.addLayout(bottom_layout)

    def back_to_booking_details(self):
        self.controller.show_view("booking_details")

    async def submit_changes(self):
        #create databaseconnection
        db_instance = dataBase()
        
        reservation = self.reservation
        roomType = self.room_type_combo.currentText()
        checkIn = self.checkin_date.date()
        checkOut = self.checkout_date.date()
        adults = self.guests_combo.currentText()

        await db_instance.change_reservation(reservation,roomType,checkIn,checkOut,adults)
        
        print(f"Booking changes submitted:\nRoom Type: {self.room_type_combo.currentText()}, Check-in: {self.checkin_date.date().toString('yyyy-MM-dd')}, Check-out: {self.checkout_date.date().toString('yyyy-MM-dd')}, Guests: {self.guests_combo.currentText()}")
        self.controller.show_view("booking_details")
        self.show_confirmation_dialog()
        
    def show_confirmation_dialog(self):
        confirmation_dialog = QMessageBox(self)
        confirmation_dialog.setWindowTitle("Changes Submitted")
        confirmation_dialog.setText("Your booking changes have been successfully submitted.")
        confirmation_dialog.setIcon(QMessageBox.Information)
        confirmation_dialog.setStandardButtons(QMessageBox.Ok)
        confirmation_dialog.exec_()

        self.controller.show_view("booking_details")
