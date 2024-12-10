import sys

from PySide6 import QtWidgets

from morsecode.arduino_device import list_resources
from morsecode.morsecode import MorseCode


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
        self.print_button = QtWidgets.QPushButton("print")

        vbox.addWidget(self.receiving_box)

        vbox.addWidget(self.print_button)

        # what happens when the print button is clicked
        self.print_button.clicked.connect(self.print_message)

        # creates a choice for the arduino port
        self.select_arduino_label = QtWidgets.QLabel("Port")
        self.select_arduino_combobox = QtWidgets.QComboBox()

        vbox.addWidget(self.select_arduino_label)
        vbox.addWidget(self.select_arduino_combobox)

        ports = list_resources()

        self.select_arduino_combobox.addItems(ports)

    def print_message(self, port):
        port = self.select_arduino_combobox.currentText()
        device = MorseCode(port)

        message = device.receive_message()

        # # text = str("This is a placeholder text")
        self.receiving_box.append(f"Sender:  {message}")

        device.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
