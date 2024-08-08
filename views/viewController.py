# viewcontroller.py
from PyQt5.QtWidgets import QStackedWidget

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