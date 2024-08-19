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
from PyQt5.QtCore import QDate, QTime, QDateTime
from views.Page_1_mainWindow import MainWindow
from classes.customer import Customer
from classes.reservation import Reservation
from classes.room import Room
from views.BookingDetailsWindow import BookingDetailsWindow
from views.CancelBookingDialog import CancelBookingDialog
from views.ChangeBookingWindow import ChangeBookingWindow
from qasync import QEventLoop
import asyncio
import pydoc

class main():

    def run_tests(self):
        passed_tests = 0
        failed_tests = 0

        def assert_and_track(condition, test_name):
            nonlocal passed_tests, failed_tests
            try:
                assert condition
                print(f"{test_name} passed.")
                passed_tests += 1
            except AssertionError:
                print(f"{test_name} failed.")
                failed_tests += 1

        # Test Customer input
        customer = Customer()
        customer.set_name("John Doe")
        customer.set_email("john.doe@example.com")
        customer.set_persons(2)
        assert_and_track(customer.get_name() == "John Doe", "Customer name test")
        assert_and_track(customer.get_email() == "john.doe@example.com", "Customer email test")
        assert_and_track(customer.get_persons() == 2, "Customer persons test")

        # Test Reservation input
        reservation = Reservation()
        reservation.setCustomer(customer)
        reservation.setRoomName("Suite")
        reservation.setConfirmation("CONF12345")
        reservation.setPersons(2)
        assert_and_track(reservation.getCustomer().get_name() == "John Doe", "Reservation customer name test")
        assert_and_track(reservation.getRoomName() == "Suite", "Reservation room name test")
        assert_and_track(reservation.getConfirmation() == "CONF12345", "Reservation confirmation test")
        assert_and_track(reservation.getPersons() == 2, "Reservation persons test")

        # Test BookingDetailsWindow input
        qdate1 = QDate(2024, 9, 1)
        qdate2 = QDate(2024, 9, 5)
        qdatetime1 = QDateTime(qdate1).toPyDateTime()
        qdatetime2 = QDateTime(qdate2).toPyDateTime()

        reservation_details = {"confirmationNumber": "CONF12345", "checkIn": qdatetime1, "checkOut": qdatetime2}
        customer_details = {"name": "John Doe", "email": "john.doe@example.com"}
        room_details = {"type": "Suite", "price": 200}
        booking_window = BookingDetailsWindow(reservation_details, customer_details, room_details, room_details, None)
        assert_and_track(booking_window.customer["name"] == "John Doe", "BookingDetailsWindow customer name test")
        assert_and_track(booking_window.room["type"] == "Suite", "BookingDetailsWindow room type test")

        # Test CancelBookingDialog input
        cancel_dialog = CancelBookingDialog(booking_window, None)
        cancel_dialog.booking_details_window.reservation = reservation_details
        assert_and_track(cancel_dialog.booking_details_window.reservation["confirmationNumber"] == "CONF12345", "CancelBookingDialog confirmation test")

        # Test ChangeBookingWindow input
        change_window = ChangeBookingWindow(reservation_details, customer_details, room_details, None)
        assert_and_track(change_window.customer["name"] == "John Doe", "ChangeBookingWindow customer name test")
        assert_and_track(change_window.roomType["type"] == "Suite", "ChangeBookingWindow room type test")

        # Print summary of test results
        print(f"\nTest Summary: {passed_tests} passed, {failed_tests} failed.")

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
    main_app.run_tests()  # Run the tests
    main_app.run()