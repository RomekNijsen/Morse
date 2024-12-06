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

        # creates horizontal layout ( 1 box next to another one)
        hbox = QtWidgets.QHBoxLayout(central_widget)

        # creates vertical layout in horizontal one for the send buttons
        vbox_send = QtWidgets.QVBoxLayout()
        hbox.addLayout(vbox_send)

        # creates the input box and send button and adds them to vertical layout
        self.input_box = QtWidgets.QTextEdit()
        self.send_button = QtWidgets.QPushButton("Send")

        vbox_send.addWidget(self.input_box)
        vbox_send.addWidget(self.send_button)

        # creates the history box, where the text history is shown
        self.history_box = QtWidgets.QTextEdit()
        hbox.addWidget(self.history_box)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
