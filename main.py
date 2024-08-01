import sys
from PyQt5.QtWidgets import QApplication
from Page_1_mainWindow import MainWindow
from qasync import QEventLoop
import asyncio

class main():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loop = QEventLoop(self.app)
        asyncio.set_event_loop(self.loop)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        with self.loop:
            self.loop.run_forever()

if __name__ == "__main__":
    main_app = main()
    main_app.run()