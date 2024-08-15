"""
The window that is opened from main window -> booking window.
Lets the user overview the available room types, how many guests they can fit in.
"""
# main window -> booking window -> booking rooms window
"""
class: BookingRoomsWindow
most recent update: 8/8/2024

programmers: Harold Flint

Description:
The BookingRoomsWindow class is opened from the MainWindow through the BookingWindow.
It allows the user to overview the available room types, see how many guests each room can accommodate,
and select a room for booking.
"""
from functools import partial
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from views.Page_4_RoomBookingDetailsWindow import RoomBookingDetailsWindow
import pydoc

class BookingRoomsWindow(QWidget):
    """""
    This window presents the user with a selection of room options, including details such as room name, 
    type, number of guests it can accommodate, and price per night. The user can then proceed to book a room 
    or return to the previous booking window.

    Attributes:
        controller (ViewController): Manages view transitions and interactions with other views.
        rooms (list): A list of dictionaries representing available room options, including name, type, capacity, price, and image.
    
    Methods:
        back_to_booking(): Navigates back to the BookingWindow.
        open_room_booking_details(room, newReservation, guests): Opens the RoomBookingDetailsWindow to finalize the booking details for the selected room.
    """""

    def __init__(self, newReservation, guests, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Booking")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #5F493F")

        # widgets will be stacked vertically
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # spacer item to push the room options layout to the center vertically
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        # center container to hold the room options layout
        center_container = QHBoxLayout()
        center_container.addStretch()

        # horizontal layour for the room boxes
        room_options_layout = QHBoxLayout()
        main_layout.addLayout(room_options_layout)
        
        center_widget = QWidget()
        center_widget.setLayout(center_container)
        main_layout.addWidget(center_widget)

        rooms = [
            {"name": "Premiere Harold Single", "type": "Single", "sleeps": 1, "price": 75, "image": "resources/single.jpg"},
            {"name": "Premiere Harold Double", "type": "Double", "sleeps": 4, "price": 125, "image": "resources/double.jpg"},
            {"name": "Premiere Harold Suite", "type": "Suite", "sleeps": 4, "price": 200, "image": "resources/suite.jpeg"}
        ]
        # styling each room box
        for room in rooms:
            room_layout = QVBoxLayout()
            room_frame = QFrame()
            room_frame.setLayout(room_layout)
            room_frame.setStyleSheet("background-color: white; padding: 10px; border-radius: 10px;")
            room_frame.setFixedSize(250, 450)

            # settings for the picture
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
            # connecting the "book now" button to open the next window
            book_now_button.clicked.connect(partial(self.open_room_booking_details, room, newReservation, guests))
            # adding the button to the layout
            room_layout.addWidget(book_now_button)

            # adding a div with each room to the room layout
            room_options_layout.addWidget(room_frame)

        # space for the "back" button
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)

        # Add the back button to the bottom right corner
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        
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
        # back button brings the user to the previous frame
        back_button.clicked.connect(self.back_to_booking)
        bottom_layout.addWidget(back_button)
        main_layout.addLayout(bottom_layout)

    def back_to_booking(self):
        self.controller.show_view("booking")

    def open_room_booking_details(self, room, newReservation, guests):
        self.room_booking_details_window = RoomBookingDetailsWindow(room, newReservation, guests, self.controller)
        self.controller.add_view(self.room_booking_details_window, "room_booking_details")
        self.controller.show_view("room_booking_details")