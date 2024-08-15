# main window -> check booking -> cancel booking -> booking canceled
"""
class: BookingCanceledDialog
most recent update: 8/12/2024
programmers: Harold Flint

Description:
The BookingCanceledDialog class is a confirmation dialog that appears after a user successfully cancels their booking. 
It provides a simple interface that informs the user that their booking has been canceled and offers a single "Close" 
button to return to the main window.
"""
"""""
a confirmation window for canceling
"""""
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
import pydoc

class BookingCanceledDialog(QDialog):
    """
    This dialog is the final step in the booking cancellation process, ensuring the user receives feedback that the cancellation 
    has been processed.

    Attributes:
        controller (ViewController): Manages view transitions and interactions with other views.

    Methods:
        close_dialog(): Closes the dialog and navigates back to the MainWindow.
        center_dialog(): Centers the dialog on the parent window.   
    """
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("Booking Canceled")
        self.setFixedSize(300, 300)
        self.setStyleSheet("background-color: #E5D5C3;")

        layout = QVBoxLayout()

        # Confirmation message
        message = QLabel("Your booking has been successfully canceled.")
        message.setAlignment(Qt.AlignCenter)
        message.setStyleSheet("color: black;")
        layout.addWidget(message)

        # Close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
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
        close_button.clicked.connect(self.close_dialog)
        layout.addWidget(close_button)

        self.setLayout(layout)
        self.center_dialog()

    def close_dialog(self):
        self.accept()
        self.controller.show_view("main")

    def center_dialog(self):
        parent_rect = self.booking_details_window.geometry()
        dialog_rect = self.geometry()
        center_point = parent_rect.center() - dialog_rect.center()
        self.move(parent_rect.topLeft() + center_point)