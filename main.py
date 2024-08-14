# main.py
"""
    The main class initializes and runs the PyQt5 application.

    This class sets up the QApplication, integrates it with an asyncio event loop using QEventLoop,
    and displays the main window of the application.

    Attributes:
    -----------
    app : QApplication
        The main application object that manages application-wide settings and resources.
    loop : QEventLoop
        The event loop that integrates asyncio with the PyQt5 application.
    window : MainWindow
        The main window of the application, defined in the Page_1_mainWindow module.
    """

import sys
from PyQt5.QtWidgets import QApplication
from views.Page_1_mainWindow import MainWindow
from qasync import QEventLoop
import asyncio
import pydoc

class main():
    def __init__(self):
        """
        Initializes the main application, sets up the event loop, and creates the main window.
        """
        self.app = QApplication(sys.argv)
        self.loop = QEventLoop(self.app)
        asyncio.set_event_loop(self.loop)
        self.window = MainWindow()

    def run(self):
        """
        Runs the application by showing the main window and starting the event loop.

        This method displays the main window and enters the application's event loop, which
        remains active until the application is closed.
        """
        self.window.show()
        with self.loop:
            self.loop.run_forever()

if __name__ == "__main__":
    main_app = main()
    main_app.run()
