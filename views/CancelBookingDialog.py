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
        #confirming the cancel
        yes_button.clicked.connect(self.confirm_cancel)
        # add the button to the button layout
        buttons_layout.addWidget(yes_button)

        # no button
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
        # the dialog will close 
        no_button.clicked.connect(self.reject)  
        buttons_layout.addWidget(no_button)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        self.center_dialog()

    # the dialog appears in the middle of the parent window
    def center_dialog(self):
        parent_rect = self.booking_details_window.geometry()
        dialog_rect = self.geometry()
        center_point = parent_rect.center() - dialog_rect.center()
        self.move(parent_rect.topLeft() + center_point)

    def confirm_cancel(self):
        # Placeholder for canceling the booking in the database
        print("Booking canceled. Placeholder for database operation.")
        self.accept()  # Close the dialog

        # After canceling, go back to the main window or any other appropriate window
        self.controller.show_view("main")