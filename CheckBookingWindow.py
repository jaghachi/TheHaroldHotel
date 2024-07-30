from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from BookingDetailsWindow import BookingDetailsWindow

class CheckBookingWindow(QWidget):
    def __init__(self):
        super().__init__()
         # a new window where the user can input their reservation confirmation #
        self.setWindowTitle("Check your reservation")
        self.setFixedSize(300, 150)
        self.setStyleSheet("background-color: #765A45;")

        main_layout = QVBoxLayout()

        title = QLabel("Input your Confirmation Number: ")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; color: white;")
        main_layout.addWidget(title)

        self.confirmation_input = QLineEdit(self)
        self.confirmation_input.setStyleSheet("background-color: white; color: black; padding: 5px;")
        main_layout.addWidget(self.confirmation_input)

        # the button "check booking"
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
        # connected the button to open a new window
        check_button.clicked.connect(self.check_booking)
        main_layout.addWidget(check_button)

        # in case the confirmation # doesn't exist, display a red text below
        self.error_label = QLabel("")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setStyleSheet("font-size: 10px; color: red;")
        main_layout.addWidget(self.error_label)

        self.setLayout(main_layout)

    # check if the booking exists
    def check_booking(self):
        confirmation_number = self.confirmation_input.text().strip()
        print(f"Checking booking for confirmation number: {confirmation_number}")

        # Placeholder logic for checking the booking, set to false rn
        booking_exists = False  

        # opens a new window with booking details
        if booking_exists:
            self.booking_details_window = BookingDetailsWindow(confirmation_number)
            self.booking_details_window.show()
            # will display the error message
        else:
            self.error_label.setText("Confirmation number not found. Please try again.")
