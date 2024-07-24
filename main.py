import sys
from mainWindow import MainWindow

def main():
    app = QApplication(sys.argv)

    # logo for running app
    app.setWindowIcon(QIcon("shmogo.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()