# viewcontroller.py
from PyQt5.QtWidgets import QStackedWidget
from views.CheckBookingWindow import CheckBookingWindow
from views.Page_2_BookingWindow import BookingWindow


class ViewController(QStackedWidget):
    def __init__(self):
        super().__init__()

    def add_view(self, widget, name):
        self.addWidget(widget)
        widget.name = name

    def show_view(self, name):
        for i in range(self.count()):
            if self.widget(i).name == name:
                self.setCurrentIndex(i)
                break
    
    def remove_view(self, name):
        for i in range(self.count()):
            if self.widget(i).name == name:
                widget_to_remove = self.widget(i)
                self.removeWidget(widget_to_remove)
                widget_to_remove.deleteLater()
                break
    
    def clear_views(self, controller):
        controller.remove_view("booking")
        controller.remove_view("check_booking")
        controller.remove_view("room_booking_details")
        controller.remove_view("booking_rooms")
        controller.remove_view("confirmation")
        controller.remove_view("booking_details")
    
    def readd_views(self, controller):
        self.booking_view = BookingWindow(controller)
        controller.add_view(controller.booking_view, "booking")

        self.check_booking_view = CheckBookingWindow(controller)
        controller.add_view(controller.check_booking_view, "check_booking")
        