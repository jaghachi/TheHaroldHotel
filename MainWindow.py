import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QAction, QVBoxLayout, QHBoxLayout, QPushButton, QDateEdit, QComboBox
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QPoint
from BookingWindow import BookingWindow
from CheckBookingWindow import CheckBookingWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup the main window
        self.setWindowTitle("The Harold Hotels")
        self.setGeometry(100, 100, 800, 600)
        
        # background pic + position
        self.background = QPixmap("lobby.jpg")
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # a line for the logo + its color
        self.white_line = QLabel(self)
        self.white_line.setStyleSheet("background-color: #E5D5C3;")
        
        # scaling the logo
        self.logo = QPixmap("shmogo.png")
        self.scaled_logo = self.logo.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(self.scaled_logo)

        # the options on the bottom of the window
        self.text_label1 = QLabel("Booking", self)
        self.text_label2 = QLabel("Rooms", self)
        self.text_label3 = QLabel("Info", self)

        # style for the text
        font = QFont("Georgia", 24)
        self.text_label1.setFont(font)
        self.text_label2.setFont(font)
        self.text_label3.setFont(font)
        
        self.text_label1.setStyleSheet("color: black")
        self.text_label2.setStyleSheet("color: black")
        self.text_label3.setStyleSheet("color: black")

        # creating a drop down menu from the "booking" with 2 options "book a room" and "check your booking"
        self.menu = QMenu(self)
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

        self.book_room_action.triggered.connect(self.open_booking_window)
        self.check_booking_action.triggered.connect(self.open_check_booking_window)
        
        self.adjust_images()

    # scales everything when the size of the window is changes
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_images()

    def adjust_images(self):
        # scales the background image to fit the window
        new_background = self.background.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # sets QLabel to make the pic a background
        self.background_label.setPixmap(new_background)
        # position the background at the top left corner
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        line_height = 100
        line_y_position = (self.height() - line_height) // 2 
        self.white_line.setGeometry(0, line_y_position, self.width(), line_height)

        logo_width = self.scaled_logo.width()
        logo_height = self.scaled_logo.height()
        # position the line in the middle of the window
        x_center = (self.width() - logo_width) // 2
        y_center = (self.height() - logo_height) // 2
        self.logo_label.setGeometry(x_center, y_center, logo_width, logo_height)

        # position of the bottom menu options (text)
        text_height = 25
        bottom_margin = 20
        spacing = 80


        # calculates the spacing between the text labels so they are centered
        total_text_width = self.text_label1.width() + self.text_label2.width() + self.text_label3.width() + 2 * spacing
        # calculates the position so the text is centered
        text_x_start = (self.width() - total_text_width) // 2

         # calculates the start of the each label for center
        self.text_label1.setGeometry(text_x_start, self.height() - text_height - bottom_margin, self.text_label1.width(), text_height)
        self.text_label2.setGeometry(text_x_start + self.text_label1.width() + spacing, self.height() - text_height - bottom_margin, self.text_label2.width(), text_height)
        self.text_label3.setGeometry(text_x_start + self.text_label1.width() + self.text_label2.width() + 2 * spacing, self.height() - text_height - bottom_margin, self.text_label3.width(), text_height)

    # for the drop-down menu 
    def eventFilter(self, source, event):
        # if the mouse hovers over the "booking" label
        if event.type() == event.Enter and source == self.text_label1:
            # calculating the position for the drop-down menu to appear
            pos = self.text_label1.mapToGlobal(QPoint(0, 0))
            self.menu.exec_(pos + QPoint(0, -self.menu.sizeHint().height()))
        return super().eventFilter(source, event)

    # when in drop-down menu, the user clicks "book a room" option
    def open_booking_window(self):
        # creates a new window
        self.booking_window = BookingWindow()
        # ensures that the user interacts with this window before touching other windows
        
        # position the booking window in the center of the parent (main window)
        parent_rect = self.rect()
        # calculates the center of the parent div
        parent_center = parent_rect.center()
        booking_rect = self.booking_window.rect()
        # moving the center of the pop-up window to the center of the parent using the parent's coordinates
        booking_rect.moveCenter(parent_center)
        # adjust for global screen coordinates
        self.booking_window.move(booking_rect.topLeft() + self.pos())
        # making the pop-up window visible
        self.booking_window.show()


    # when user clicks on the "check booking" option from the drop-down menu
    def open_check_booking_window(self):
        # creating a pop-up window
        self.check_booking_window = CheckBookingWindow()
        parent_rect = self.rect()
        # calculating the center of the parent window for the pop-up window
        parent_center = parent_rect.center()
        check_booking_rect = self.check_booking_window.rect()
        check_booking_rect.moveCenter(parent_center)
        self.check_booking_window.move(check_booking_rect.topLeft() + self.pos())
        self.check_booking_window.show()