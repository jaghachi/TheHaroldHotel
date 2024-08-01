from hmac import new
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from reservation import Reservation
from Page_5_BookingConfirmationWindow import BookingConfirmationWindow


# booking + room details
class RoomBookingDetailsWindow(QWidget):
    def __init__(self, room, newReservation, adults):
        super().__init__()
        self.setWindowTitle(f"{room["name"]} Booking")
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet("background-color: #E5D5C3")

        # Main layout, boxes for pics
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Room images
        room_image_label = QLabel()
        pixmap = QPixmap(room["image"]).scaled(300, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        room_image_label.setPixmap(pixmap)
        room_image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(room_image_label)

        # Booking details
        details_label = QLabel(f"Booking for {adults} people\nCheck-in: {newReservation.checkin_date.toString('MMM d, yyyy')} - Check-out: {newReservation.checkout_date.toString('MMM d, yyyy')}")
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
        
        # Input the email
        email_label = QLabel("Enter the email for the booking: ")
        email_label.setStyleSheet("font-size: 18px; color: black;")
        email_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(email_label)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Your email")
        main_layout.addWidget(self.email_input)

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
        book_button.clicked.connect(lambda: self.open_booking_confirmation(room, newReservation, adults, self.name_input.text(), self.email_input.text()))
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

    async def open_booking_confirmation(self, room, newReservation, adults, user_name, user_email):
        
        bookedReservation = newReservation.reserveRoom(room, newReservation, adults, user_name, user_email)
        
        
        self.confirmation_window = BookingConfirmationWindow(bookedReservation)
        self.confirmation_window.setWindowModality(Qt.ApplicationModal)
        self.confirmation_window.show()