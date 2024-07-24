import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, QComboBox, QPushButton, QMainWindow, QMenu, QAction, QSizePolicy, QSpacerItem, QLineEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QDate, QPoint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # above the window name
        self.setWindowTitle("The Harold Hotels")
        self.setGeometry(100, 100, 800, 600)

        # background - lobby photo 
        self.background = QPixmap("lobby.jpg")  
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # line for the logo
        self.white_line = QLabel(self)
        self.white_line.setStyleSheet("background-color: #E5D5C3;")
        
        # logo
        self.logo = QPixmap("shmogo.png")  # Ensure shmogo.png is in the same directory
        
        # scaling the logo
        self.scaled_logo = self.logo.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(self.scaled_logo)

        # the text options
        self.text_label1 = QLabel("Booking", self)
        self.text_label2 = QLabel("Rooms", self)
        self.text_label3 = QLabel("Info", self)
        
        # the text features
        font = QFont("Georgia", 24)
        self.text_label1.setFont(font)
        self.text_label2.setFont(font)
        self.text_label3.setFont(font)
        
        # color for text
        self.text_label1.setStyleSheet("color: black")
        self.text_label2.setStyleSheet("color: black")
        self.text_label3.setStyleSheet("color: black")


        # scaling with the window
        self.adjust_images()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_images()

    def adjust_images(self):
        # resizing for backgound image (lobby)
        new_background = self.background.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.background_label.setPixmap(new_background)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # adjusting the white line and its position 
        line_height = 100
        line_y_position = (self.height() - line_height) // 2 
        self.white_line.setGeometry(0, line_y_position, self.width(), line_height)

        # position the logo in the middle of the screen
        logo_width = self.scaled_logo.width()
        logo_height = self.scaled_logo.height()
        x_center = (self.width() - logo_width) // 2
        y_center = (self.height() - logo_height) // 2
        self.logo_label.setGeometry(x_center, y_center, logo_width, logo_height)

        # the style for the text
        text_height = 25
        bottom_margin = 20
        spacing = 80

        # text position
        total_text_width = self.text_label1.width() + self.text_label2.width() + self.text_label3.width() + 2 * spacing
        text_x_start = (self.width() - total_text_width) // 2

        self.text_label1.setGeometry(text_x_start, self.height() - text_height - bottom_margin, self.text_label1.width(), text_height)
        self.text_label2.setGeometry(text_x_start + self.text_label1.width() + spacing, self.height() - text_height - bottom_margin, self.text_label2.width(), text_height)
        self.text_label3.setGeometry(text_x_start + self.text_label1.width() + self.text_label2.width() + 2 * spacing, self.height() - text_height - bottom_margin, self.text_label3.width(), text_height)

def main():
    app = QApplication(sys.argv)

    # logo for running app
    app.setWindowIcon(QIcon("shmogo.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()