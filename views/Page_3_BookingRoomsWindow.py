# bookingroomswindow.py
from functools import partial
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from views.Page_4_RoomBookingDetailsWindow import RoomBookingDetailsWindow

class BookingRoomsWindow(QWidget):
    def __init__(self, newReservation, guests, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Booking")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #E5D5C3")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        booking_details_layout = QHBoxLayout()
        dates_label = QLabel(f"Your booking: {newReservation.checkIn.toString('MMM d')} - {newReservation.checkOut.toString('MMM d')}")
        dates_label.setStyleSheet("font-size: 18px; color: black;")
        booking_details_layout.addWidget(dates_label)
        main_layout.addLayout(booking_details_layout)

        room_options_layout = QHBoxLayout()
        main_layout.addLayout(room_options_layout)

        rooms = [
            {"name": "Premiere Harold Single", "type": "Single", "sleeps": 1, "price": 75, "image": "resources/single.jpg"},
            {"name": "Premiere Harold Double", "type": "Double", "sleeps": 4, "price": 125, "image": "resources/double.jpg"},
            {"name": "Premiere Harold Suite", "type": "Suite", "sleeps": 4, "price": 200, "image": "resources/suite.jpeg"}
        ]

        for room in rooms:
            room_layout = QVBoxLayout()
            room_frame = QFrame()
            room_frame.setLayout(room_layout)
            room_frame.setStyleSheet("background-color: white; padding: 10px; border-radius: 10px;")
            room_frame.setFixedSize(250, 450)

            room_image_container = QLabel()
            room_image_container.setFixedSize(220, 200)
            room_image_container.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
            room_image_container.setAlignment(Qt.AlignCenter)

            pixmap = QPixmap(room["image"]).scaled(room_image_container.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            room_image_container.setPixmap(pixmap)
            room_layout.addWidget(room_image_container)

            room_name = QLabel(room["name"])
            room_name.setStyleSheet("font-size: 15px; color: black; font-weight: bold;")
            room_layout.addWidget(room_name)

            room_sleeps = QLabel(f"Sleeps {room['sleeps']}")
            room_sleeps.setStyleSheet("font-size: 14px; color: gray;")
            room_layout.addWidget(room_sleeps)

            room_price = QLabel(f"${room['price']} per night")
            room_price.setStyleSheet("font-size: 16px; color: black; font-weight: bold;")
            room_layout.addWidget(room_price)

            book_now_button = QPushButton("Book Now")
            book_now_button.setStyleSheet("""
                QPushButton {
                    background-color: #5F493F;
                    color: white;
                    font-size: 16px;
                    font-weight: bold;
                    padding: 10px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #E5D5C3;
                    color: black;
                }
            """)
            book_now_button.clicked.connect(partial(self.open_room_booking_details, room, newReservation, guests))
            room_layout.addWidget(book_now_button)

            room_options_layout.addWidget(room_frame)
        
        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #5F493F;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
                color: black;
            }
        """)
        back_button.clicked.connect(self.back_to_booking)
        main_layout.addWidget(back_button)

    def back_to_booking(self):
        self.controller.show_view("booking")

    def open_room_booking_details(self, room, newReservation, guests):
        self.room_booking_details_window = RoomBookingDetailsWindow(room, newReservation, guests, self.controller)
        self.controller.add_view(self.room_booking_details_window, "room_booking_details")
        self.controller.show_view("room_booking_details")