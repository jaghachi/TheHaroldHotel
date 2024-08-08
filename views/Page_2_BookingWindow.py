"""""
the window the user opens from the MainWindow when clicking on "book a room"
the window contains the check-in and check-out dates and the number of guests
"""""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, QComboBox, QPushButton, QSpacerItem, QSizePolicy, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QDate
from views.Page_3_BookingRoomsWindow import BookingRoomsWindow
from classes.reservation import Reservation

class BookingWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Book a Room")
        self.setGeometry(100, 100, 800, 600)

        # set up the background pic
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("resources/lobby.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 800, 600)

        # main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0) # no margins
        main_layout.setSpacing(0) # no spacing between widgets

        # spacer item to push the centered_frame to the middle
        spacer_top = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_top)

        # centered container for the date and guest selection widgets
        centered_frame = QFrame(self)
        centered_frame.setStyleSheet("background-color: #5F493F; border-radius: 10px;")
        centered_frame.setFixedSize(400, 300)

        centered_layout = QVBoxLayout(centered_frame)

        title = QLabel("SELECT YOUR DATES")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        # make it a part of the centered_frame
        centered_layout.addWidget(title)

        # creating layouts for check-in and check-out dates
        date_layout = QHBoxLayout() # horizontal
        checkin_layout = QVBoxLayout() # vertical
        checkout_layout = QVBoxLayout() # vertical

        checkin_label = QLabel("Check-in")
        checkin_label.setAlignment(Qt.AlignCenter)
        # borders around the check-in box
        checkin_label.setStyleSheet("border: 1px solid #FFFFFF;")
        # helps to work with dates and calendars
        self.checkin_date = QDateEdit()
        # sets the check-in date as the current date - default
        self.checkin_date.setDate(QDate.currentDate())
        self.checkin_date.setCalendarPopup(True)
        # aligning in the center of its label
        self.checkin_date.setAlignment(Qt.AlignCenter)
        # border for the check-in label
        self.checkin_date.setStyleSheet("border: 1px solid #FFFFFF;")
        # adding check-in label to the check-in box
        checkin_layout.addWidget(checkin_label)
        # addind a calendar pop-up to the check-in box
        checkin_layout.addWidget(self.checkin_date)

        checkout_label = QLabel("Check-out")
        checkout_label.setAlignment(Qt.AlignCenter)
        # border for the check-out box
        checkout_label.setStyleSheet("border: 1px solid #FFFFFF;")
        self.checkout_date = QDateEdit()
        self.checkout_date.setDate(QDate.currentDate().addDays(1))
        self.checkout_date.setCalendarPopup(True)
        self.checkout_date.setAlignment(Qt.AlignCenter)
        checkout_layout.addWidget(checkout_label)
        checkout_layout.addWidget(self.checkout_date)

        # adding the check-in layout to the horizontal date layout
        date_layout.addLayout(checkin_layout)
        # adding the check-out layout to the horizontal date layout
        date_layout.addLayout(checkout_layout)
        # adding the horizontal date layout (containing check-in and check-out) to the centered layout
        centered_layout.addLayout(date_layout)

        guests_layout = QVBoxLayout() # vertical box
        self.guests_combo = QComboBox()  # drop-down list
        self.guests_combo.addItems([str(i) for i in range(1, 6)]) # can choose up to 5 guests
        guests_label = QLabel("Guests") 
        guests_label.setAlignment(Qt.AlignCenter)
        # a border for the label
        guests_label.setStyleSheet("border: 1px solid #FFFFFF;")
        # a border for the drop-down menu
        self.guests_combo.setStyleSheet("border: 1px solid #FFFFFF;")
        # adding label and drop-down meny to the vertical box
        guests_layout.addWidget(guests_label)
        guests_layout.addWidget(self.guests_combo)
        # add the guests layout to the centers box
        centered_layout.addLayout(guests_layout)

        find_rooms_button = QPushButton("FIND ROOMS")
        find_rooms_button.setStyleSheet("""
            QPushButton {
                background-color: #E5D5C3;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5F493F;
                color: black;
            }
        """)
        # clicking on the "find rooms" button will open BookingRoomsWindow
        find_rooms_button.clicked.connect(self.open_booking_rooms_window)
        # adding a button to the centered box
        centered_layout.addWidget(find_rooms_button)

        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #E5D5C3;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5F493F;
                color: black;
            }
        """)
        # clicking on the "back" button brings user to the MainWindow
        back_button.clicked.connect(self.back_to_main)
        centered_layout.addWidget(back_button)

        # adding a "back" button to the centered frame
        centered_layout.addWidget(back_button)

        # adding the centered frame to the main layout
        center_container = QHBoxLayout()
        center_container.addStretch()
        center_container.addWidget(centered_frame)
        center_container.addStretch()
        main_layout.addLayout(center_container)

        # spacer item to push the centered_frame to the middle
        spacer_bottom = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer_bottom)

        self.setLayout(main_layout)

    # connect to the next window
    def open_booking_rooms_window(self):
        newReservation = Reservation()
        newReservation.checkIn = self.checkin_date.date()
        newReservation.checkOut = self.checkout_date.date()
        guests = int(self.guests_combo.currentText())

        self.booking_rooms_view = BookingRoomsWindow(newReservation, guests, self.controller)
        self.controller.add_view(self.booking_rooms_view, "booking_rooms")
        self.controller.show_view("booking_rooms")

    # back button
    def back_to_main(self):
        self.controller.show_view("main")
