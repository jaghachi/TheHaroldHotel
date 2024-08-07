# mainwindow.py
from PyQt5.QtWidgets import QMainWindow, QLabel, QMenu, QAction, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QPoint
from views.viewController import ViewController
from views.Page_2_BookingWindow import BookingWindow
from views.CheckBookingWindow import CheckBookingWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Harold Hotel")
        self.setGeometry(100, 100, 800, 600)
        
        self.controller = ViewController()
        self.setCentralWidget(self.controller)

        self.main_view = QWidget()
        self.main_layout = QVBoxLayout(self.main_view)
        
        # Setup for main view
        self.setup_main_view()

        # Add views to controller
        self.controller.add_view(self.main_view, "main")

        self.booking_view = BookingWindow(self.controller)
        self.controller.add_view(self.booking_view, "booking")

        self.check_booking_view = CheckBookingWindow(self.controller)
        self.controller.add_view(self.check_booking_view, "check_booking")

    def setup_main_view(self):
        # Background and logo setup
        self.background = QPixmap("resources/lobby.jpg")
        self.background_label = QLabel(self.main_view)
        self.background_label.setPixmap(self.background)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        self.white_line = QLabel(self.main_view)
        self.white_line.setStyleSheet("background-color: #E5D5C3;")

        self.logo = QPixmap("resources/shmogo.png")
        self.scaled_logo = self.logo.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label = QLabel(self.main_view)
        self.logo_label.setPixmap(self.scaled_logo)

        # Bottom menu options
        self.text_label1 = QLabel("Booking", self.main_view)
        self.text_label2 = QLabel("Rooms", self.main_view)
        self.text_label3 = QLabel("Info", self.main_view)

        font = QFont("Georgia", 24)
        self.text_label1.setFont(font)
        self.text_label2.setFont(font)
        self.text_label3.setFont(font)
        
        self.text_label1.setStyleSheet("color: black")
        self.text_label2.setStyleSheet("color: black")
        self.text_label3.setStyleSheet("color: black")

        self.menu = QMenu(self.main_view)
        self.menu.setStyleSheet("""
            QMenu {
                background-color: white;
                color: black;
                font-family: 'Georgia';
                font-size: 18px;
            }
            QMenu::item {
                background-color: white;
                color: black;
            }
            QMenu::item:selected {
            background-color: #E5D5C3;
            color: black;
            }
        """)

        self.book_room_action = QAction("Book a room", self.menu)
        self.check_booking_action = QAction("Check your booking", self.menu)
        self.menu.addAction(self.book_room_action)
        self.menu.addAction(self.check_booking_action)
        self.text_label1.installEventFilter(self)

        self.book_room_action.triggered.connect(self.open_booking_view)
        self.check_booking_action.triggered.connect(self.open_check_booking_view)
        
        self.adjust_images()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_images()

    def adjust_images(self):
        new_background = self.background.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.background_label.setPixmap(new_background)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        line_height = 100
        line_y_position = (self.height() - line_height) // 2 
        self.white_line.setGeometry(0, line_y_position, self.width(), line_height)

        logo_width = self.scaled_logo.width()
        logo_height = self.scaled_logo.height()
        x_center = (self.width() - logo_width) // 2
        y_center = (self.height() - logo_height) // 2
        self.logo_label.setGeometry(x_center, y_center, logo_width, logo_height)

        text_height = 25
        bottom_margin = 20
        spacing = 80

        total_text_width = self.text_label1.width() + self.text_label2.width() + self.text_label3.width() + 2 * spacing
        text_x_start = (self.width() - total_text_width) // 2

        self.text_label1.setGeometry(text_x_start, self.height() - text_height - bottom_margin, self.text_label1.width(), text_height)
        self.text_label2.setGeometry(text_x_start + self.text_label1.width() + spacing, self.height() - text_height - bottom_margin, self.text_label2.width(), text_height)
        self.text_label3.setGeometry(text_x_start + self.text_label1.width() + self.text_label2.width() + 2 * spacing, self.height() - text_height - bottom_margin, self.text_label3.width(), text_height)

    def eventFilter(self, source, event):
        if event.type() == event.Enter and source == self.text_label1:
            pos = self.text_label1.mapToGlobal(QPoint(0, 0))
            self.menu.exec_(pos + QPoint(0, -self.menu.sizeHint().height()))
        return super().eventFilter(source, event)

    def open_booking_view(self):
        self.controller.show_view("booking")

    def open_check_booking_view(self):
        self.controller.show_view("check_booking")
        
    def reset_fields(self):
        # Reset any specific fields if necessary in the main view
        pass
