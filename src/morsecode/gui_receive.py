import csv
import sys

import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):

    def __init__(self):
        # initialises parent class QtWidgets.QMainWindow
        super().__init__()

        # create central widget
        central_widget = QtWidgets.QWidget()
        # set central widget
        self.setCentralWidget(central_widget)

        vbox = QtWidgets.QVBoxLayout(central_widget)

        # creates output box
        self.receiving_box = QtWidgets.QTextEdit()
        self.print_button = QtWidgets.QPushButton("Print")

        vbox.addWidget(self.receiving_box)
        vbox.addWidget(self.print_button)

        # what happens when the print button is clicked
        self.print_button.clicked.connect(self.print_message)

    def print_message(self):

        text = str("This is a placeholder text")
        self.receiving_box.append(f"Sender:  {text}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
