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