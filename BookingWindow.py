from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, QComboBox, QPushButton
from PyQt5.QtCore import Qt, QDate
from BookingRoomsWindow import BookingRoomsWindow

# Pop-up window with calendar to choose dates + number of guests
class BookingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book a Room")
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color: #765A45;")

        # Main layout
        main_layout = QVBoxLayout()

        # Title
        title = QLabel("SELECT YOUR DATES")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        main_layout.addWidget(title)

        # Check-in and Check-out dates
        # creating box sections
        date_layout = QHBoxLayout()
        checkin_layout = QVBoxLayout()
        checkout_layout = QVBoxLayout()

        checkin_label = QLabel("Check-in")
        checkin_label.setAlignment(Qt.AlignCenter)
        self.checkin_date = QDateEdit()
        # sets the initial date to the current date
        self.checkin_date.setDate(QDate.currentDate())
        # initiates a calendar pop-up
        self.checkin_date.setCalendarPopup(True)
        self.checkin_date.setAlignment(Qt.AlignCenter)
        # adding the labels into the layouts 
        checkin_layout.addWidget(checkin_label)
        checkin_layout.addWidget(self.checkin_date)

        checkout_label = QLabel("Check-out")
        checkout_label.setAlignment(Qt.AlignCenter)
        # a date picker widget
        self.checkout_date = QDateEdit()
        # sets a check-out date as the current date + 1 day
        self.checkout_date.setDate(QDate.currentDate().addDays(1))
        # creating a pop-up calendar
        self.checkout_date.setCalendarPopup(True)
        self.checkout_date.setAlignment(Qt.AlignCenter)
        # adding the text into the corresponding boxes
        checkout_layout.addWidget(checkout_label)
        checkout_layout.addWidget(self.checkout_date)

        # putting the boxes into the layout
        date_layout.addLayout(checkin_layout)
        date_layout.addLayout(checkout_layout)

        main_layout.addLayout(date_layout)

        # Guests layout
        guests_layout = QVBoxLayout()

        self.guests_combo = QComboBox()
        # adding the items from 1 to 5 in the created box
        self.guests_combo.addItems([str(i) for i in range(1, 6)])
        guests_label = QLabel("Guests")
        guests_label.setAlignment(Qt.AlignCenter)
        # adding the label and number of guests in the boxes
        guests_layout.addWidget(guests_label)
        guests_layout.addWidget(self.guests_combo)

        # position everything in the main layout
        main_layout.addLayout(guests_layout)

        # find Rooms button
        find_rooms_button = QPushButton("FIND ROOMS")
        find_rooms_button.setStyleSheet("""
            QPushButton {
                background-color:  #2B1C19;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #E5D5C3;
            }
        """)
        find_rooms_button.clicked.connect(self.open_booking_rooms_window)
        main_layout.addWidget(find_rooms_button)

        self.setLayout(main_layout)

    def open_booking_rooms_window(self):
        # using the dates from our calendar widget
        checkin_date = self.checkin_date.date()
        checkout_date = self.checkout_date.date()
        # using the number of guests from our guests popup
        guests = int(self.guests_combo.currentText())

        # instance of the class
        self.booking_rooms_window = BookingRoomsWindow(checkin_date, checkout_date, guests)
        
        # creating a new window
        parent_rect = self.rect()
        parent_center = parent_rect.center()
        booking_rooms_rect = self.booking_rooms_window.rect()
        booking_rooms_rect.moveCenter(parent_center)
        self.booking_rooms_window.move(booking_rooms_rect.topLeft() + self.pos())
        self.booking_rooms_window.show()
