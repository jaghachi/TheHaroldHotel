from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class CheckBookingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check your reservation")
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color: #765A45;")

        main_layout = QVBoxLayout()

        title = QLabel("Input your Confirmation Number: ")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; color: white;")
        main_layout.addWidget(title)

        self.confirmation_input = QLineEdit(self)
        self.confirmation_input.setStyleSheet("background-color: white; color: black; padding: 5px;")
        main_layout.addWidget(self.confirmation_input)

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
        main_layout.addWidget(check_button)

        self.setLayout(main_layout)