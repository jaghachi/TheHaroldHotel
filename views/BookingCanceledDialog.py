"""""
a confirmation window for canceling
"""""
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class BookingCanceledDialog(QDialog):
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

