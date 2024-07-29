# types of room window
class BookingRoomsWindow(QWidget):
    def __init__(self, checkin_date, checkout_date, guests):
        super().__init__()
        self.setWindowTitle("Booking")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #E5D5C3")

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        booking_details_layout = QHBoxLayout()

        # Dates for booking
        dates_label = QLabel(f"Your booking: {checkin_date.toString('MMM d')} - {checkout_date.toString('MMM d')}")
        dates_label.setStyleSheet("font-size: 18px; color: black;")
        booking_details_layout.addWidget(dates_label)

        main_layout.addLayout(booking_details_layout)

        # Room options
        room_options_layout = QHBoxLayout()
        main_layout.addLayout(room_options_layout)

        rooms = [
            {"name": "Premiere Harold Single", "sleeps": 1, "price": 75, "image": "single.jpg"},
            {"name": "Premiere Harold Double", "sleeps": 4, "price": 125, "image": "double.jpg"},
            {"name": "Premiere Harold Suite", "sleeps": 4, "price": 200, "image": "suite.jpeg"}
        ]