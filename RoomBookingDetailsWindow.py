from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from BookingConfirmationWindow import BookingConfirmationWindow

# booking + room details
class RoomBookingDetailsWindow(QWidget):
    def __init__(self, room_name, room_image, checkin_date, checkout_date, adults):
        super().__init__()
        self.setWindowTitle(f"{room_name} Booking")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet("background-color: #E5D5C3")

        # Main layout, boxes for pics
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Room images
        room_image_label = QLabel()
        pixmap = QPixmap(room_image).scaled(300, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        room_image_label.setPixmap(pixmap)
        room_image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(room_image_label)

        # Booking details
        details_label = QLabel(f"Booking for {adults} people\nCheck-in: {checkin_date.toString('MMM d, yyyy')} - Check-out: {checkout_date.toString('MMM d, yyyy')}")
        details_label.setStyleSheet("font-size: 18px; color: black;")
        details_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(details_label)

        # Input the name
        name_label = QLabel("Enter the name for the booking: ")
        name_label.setStyleSheet("font-size: 18px; color: black;")
        name_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(name_label)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Your Name")
        main_layout.addWidget(self.name_input)

        # Buttons
        buttons_layout = QHBoxLayout()
        
        # Book-button
        book_button = QPushButton("Book")
        book_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        book_button.clicked.connect(lambda: self.open_booking_confirmation(room_name, checkin_date, checkout_date, adults))
        buttons_layout.addWidget(book_button)

        # Back-button
        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        back_button.clicked.connect(self.close)  # Close the current window
        buttons_layout.addWidget(back_button)

        main_layout.addLayout(buttons_layout)

    def open_booking_confirmation(self, room_name, checkin_date, checkout_date, adults):
        user_name = self.name_input.text()
        self.confirmation_window = BookingConfirmationWindow(room_name, checkin_date, checkout_date, adults, user_name)
        self.confirmation_window.setWindowModality(Qt.ApplicationModal)
        self.confirmation_window.show()