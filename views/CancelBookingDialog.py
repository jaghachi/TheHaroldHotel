# main window -> check booking -> cancel booking
"""
class: CancelBookingDialog
most recent update: 8/13/2024
programmers: Mariia Kim

Description:
The CancelBookingDialog class is a confirmation dialog that appears when the user selects the option to cancel a booking from the CheckBookingWindow. 
It prompts the user with a message asking if they are sure they want to cancel their booking, providing 'Yes' and 'No' options.
"""
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from databaseFiles.databaseconnect import dataBase
import asyncio
import pydoc

class CancelBookingDialog(QDialog):
    """
    If the user confirms the cancellation, the booking is canceled (in the actual implementation, this would involve interacting with the database), 
    and a confirmation dialog (BookingCanceledDialog) is shown. If the user selects 'No,' the dialog simply closes without any further action.

    Attributes:
        booking_details_window (QWidget): The parent window from which the cancellation dialog is opened.
        controller (ViewController): Manages view transitions and interactions with other views.

    Methods:
        center_dialog(): Centers the dialog on the parent window.
        confirm_cancel(): Handles the booking cancellation logic and opens the BookingCanceledDialog.
    """
    def __init__(self, booking_details_window, controller):
        super().__init__()
        self.booking_details_window = booking_details_window
        self.controller = controller

        self.setWindowTitle("Cancel Booking")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #E5D5C3;")

        layout = QVBoxLayout()

        # are you sure???
        message = QLabel("Are you sure you want to cancel your booking?")
        message.setAlignment(Qt.AlignCenter)
        message.setStyleSheet("color: black;")

        layout.addWidget(message)

        # Buttons layout
        buttons_layout = QHBoxLayout()

        # yes button
        yes_button = QPushButton("Yes")
        yes_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 14px;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        yes_button.clicked.connect(lambda: asyncio.ensure_future(
            self.confirm_cancel()))
        
        buttons_layout.addWidget(yes_button)

        no_button = QPushButton("No")
        no_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 14px;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        no_button.clicked.connect(self.reject)  
        buttons_layout.addWidget(no_button)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        self.center_dialog()

    def center_dialog(self):
        parent_rect = self.booking_details_window.geometry()
        dialog_rect = self.geometry()
        center_point = parent_rect.center() - dialog_rect.center()
        self.move(parent_rect.topLeft() + center_point)

    async def confirm_cancel(self):
        #create databaseconnection
        db_instance = dataBase()
        
        await db_instance.cancel_reservation(self.booking_details_window.reservation)
        
        
        print("Booking canceled.")
        
        self.close()
        self.controller.show_view("main")