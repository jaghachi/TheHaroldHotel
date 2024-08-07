# bookingwindow.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, QComboBox, QPushButton
from PyQt5.QtCore import Qt, QDate
from views.Page_3_BookingRoomsWindow import BookingRoomsWindow
from classes.reservation import Reservation

class BookingWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Book a Room")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #E5D5C3;")

        main_layout = QVBoxLayout()

        title = QLabel("SELECT YOUR DATES")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        main_layout.addWidget(title)

        date_layout = QHBoxLayout()
        checkin_layout = QVBoxLayout()
        checkout_layout = QVBoxLayout()

        checkin_label = QLabel("Check-in")
        checkin_label.setAlignment(Qt.AlignCenter)
        self.checkin_date = QDateEdit()
        self.checkin_date.setDate(QDate.currentDate())
        self.checkin_date.setCalendarPopup(True)
        self.checkin_date.setAlignment(Qt.AlignCenter)
        checkin_layout.addWidget(checkin_label)
        checkin_layout.addWidget(self.checkin_date)

        checkout_label = QLabel("Check-out")
        checkout_label.setAlignment(Qt.AlignCenter)
        self.checkout_date = QDateEdit()
        self.checkout_date.setDate(QDate.currentDate().addDays(1))
        self.checkout_date.setCalendarPopup(True)
        self.checkout_date.setAlignment(Qt.AlignCenter)
        checkout_layout.addWidget(checkout_label)
        checkout_layout.addWidget(self.checkout_date)

        date_layout.addLayout(checkin_layout)
        date_layout.addLayout(checkout_layout)
        main_layout.addLayout(date_layout)

        guests_layout = QVBoxLayout()
        self.guests_combo = QComboBox()
        self.guests_combo.addItems([str(i) for i in range(1, 6)])
        guests_label = QLabel("Guests")
        guests_label.setAlignment(Qt.AlignCenter)
        guests_layout.addWidget(guests_label)
        guests_layout.addWidget(self.guests_combo)
        main_layout.addLayout(guests_layout)

        find_rooms_button = QPushButton("FIND ROOMS")
        find_rooms_button.setStyleSheet("""
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
        find_rooms_button.clicked.connect(self.open_booking_rooms_window)
        main_layout.addWidget(find_rooms_button)

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
        back_button.clicked.connect(self.back_to_main)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

    def open_booking_rooms_window(self):
        newReservation = Reservation()
        newReservation.checkIn = self.checkin_date.date()
        newReservation.checkOut = self.checkout_date.date()
        guests = int(self.guests_combo.currentText())

        self.booking_rooms_view = BookingRoomsWindow(newReservation, guests, self.controller)
        self.controller.add_view(self.booking_rooms_view, "booking_rooms")
        self.controller.show_view("booking_rooms")

    def back_to_main(self):
        self.controller.show_view("main")
    