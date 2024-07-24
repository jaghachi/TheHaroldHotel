import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QFont, QIcon

from mainWindow import MainWindow

def main():
    app = QApplication(sys.argv)

    # logo for running app
    app.setWindowIcon(QIcon("resources/shmogo.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()