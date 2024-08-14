# viewcontroller.py
# viewcontroller.py
""""
class: ViewController
most recent update: 8/7/2024
programmers: Jonathan Aghachi

Description:
The ViewController class manages the different views in the application using a QStackedWidget. 
It allows for easy navigation between views, adding and removing views as needed, 
and maintaining the overall structure of the application's user interface.
"""
from PyQt5.QtWidgets import QStackedWidget
from views.CheckBookingWindow import CheckBookingWindow
from views.Page_2_BookingWindow import BookingWindow
import pydoc


class ViewController(QStackedWidget):
    """
    This class provides methods to add, show, remove, clear, and re-add views within the stacked widget.
    It's central to the application's navigation flow, ensuring that the correct view is displayed 
    based on user interactions.

    Attributes:
        None specific to the instance; inherits from QStackedWidget.

    Methods:
        add_view(widget, name): Adds a new view to the stack with a specified name.
        show_view(name): Displays the view corresponding to the given name.
        remove_view(name): Removes the view with the specified name from the stack.
        clear_views(controller): Clears specific views from the stack to reset the interface.
        readd_views(controller): Re-adds the default views to the stack after a reset.
    """
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
        