import sys

from PySide6 import QtWidgets

from morsecode.arduino_device import list_resources


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

        # what happens when the send button is clicked
        self.send_button.clicked.connect(self.sending)

        # creates the history box, where the text history is shown
        self.history_box = QtWidgets.QTextEdit()
        hbox.addWidget(self.history_box)

        # creates a choice for the arduino port
        self.select_arduino_label = QtWidgets.QLabel("Port")
        self.select_arduino_combobox = QtWidgets.QComboBox()

        vbox_send.addWidget(self.select_arduino_label)
        vbox_send.addWidget(self.select_arduino_combobox)

        ports = list_resources()

        self.select_arduino_combobox.addItems(ports)

    def sending(self):
        # get the text from the input box and append to the history box
        text = self.input_box.toPlainText()
        self.history_box.append(f"You:  {text}")

        # clear the input box for the next message
        self.input_box.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
