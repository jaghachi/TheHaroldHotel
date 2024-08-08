"""""
main window -> check booking -> bookng details window -> cancel booking
a pop-up dialogue that asks the user to confirm the cancelation
"""""
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class CancelBookingDialog(QDialog):
    def __init__(self, booking_details_window, controller):
        super().__init__()
        self.booking_details_window = booking_details_window
        self.controller = controller

        self.setWindowTitle("Cancel Booking")
        self.setFixedSize(400, 150)
        self.setStyleSheet("background-color: #E5D5C3;")

        layout = QVBoxLayout()

        # are you sure???
        message = QLabel("Are you sure you want to cancel your booking?")
        message.setAlignment(Qt.AlignCenter)
        message.setStyleSheet("color: black;")