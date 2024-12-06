import csv
import sys

import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        # initialises parent class QtWidgets.QMainWindow
        super().__init()

        # create central widget
        central_widget = QtWidgets.QWidget()
        # set central widget
        self.setCentralWidget(central_widget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

# from pythondaq.arduino_device import list_resources
# from pythondaq.diode_experiment import DiodeExperiment


# class UserInterface(QtWidgets.QMainWindow):

#     def __init__(self):
#         # initialise parent class QtWidgets.QMainWindow
#         super().__init__()

#         # create central widget
#         central_widget = QtWidgets.QWidget()
#         # set central widget
#         self.setCentralWidget(central_widget)

#         # vertical layout (1 box above the other)
#         # this creates the place where the graph goes
#         vbox = QtWidgets.QVBoxLayout(central_widget)

#         self.save_button = QtWidgets.QPushButton("Save")
#         vbox.addWidget(self.save_button)

#         self.save_button.clicked.connect(self.getSaveFileName)

#         # adds the plot to the first vertical layout
#         self.plot_widget = pg.PlotWidget()
#         vbox.addWidget(self.plot_widget)

#         # add horizontal layout under the vertical one
#         hbox_start_end = QtWidgets.QHBoxLayout()
#         vbox.addLayout(hbox_start_end)

#         # adds vertical layout in the horizontal one as to create a label
#         # to the start range button
#         vbox_start = QtWidgets.QVBoxLayout()
#         hbox_start_end.addLayout(vbox_start)

#         self.start_label = QtWidgets.QLabel("Start Value")
#         self.start_button = QtWidgets.QDoubleSpinBox()
#         self.start_button.setRange(0, 3.3)

#         vbox_start.addWidget(self.start_label)
#         vbox_start.addWidget(self.start_button)

#         # adds vertical layout in the horizontal one as to create a label
#         # to the end range button
#         vbox_end = QtWidgets.QVBoxLayout()
#         hbox_start_end.addLayout(vbox_end)

#         self.end_label = QtWidgets.QLabel("End Value")
#         self.end_button = QtWidgets.QDoubleSpinBox()
#         self.end_button.setRange(0, 3.3)

#         vbox_end.addWidget(self.end_label)
#         vbox_end.addWidget(self.end_button)

#         # adss another horizontal layout under the vertical one for the
#         # number of runs range and the scan button
#         hbox_number_device = QtWidgets.QHBoxLayout()
#         vbox.addLayout(hbox_number_device)

#         # adds vertical layout in the horizontal one as to create a label
#         # to the number range button
#         vbox_number = QtWidgets.QVBoxLayout()
#         hbox_number_device.addLayout(vbox_number)

#         self.number_label = QtWidgets.QLabel("Number of Scans")
#         self.number_button = QtWidgets.QSpinBox()
#         self.number_button.setRange(1, 1000)

#         vbox_number.addWidget(self.number_label)
#         vbox_number.addWidget(self.number_button)

#         # adds another vertical layout to the horizontal one to create
#         # button that selects the port

#         vbox_device = QtWidgets.QVBoxLayout()
#         hbox_number_device.addLayout(vbox_device)

#         self.select_arduino_label = QtWidgets.QLabel("Port")
#         self.select_arduino_button = QtWidgets.QComboBox()

#         vbox_device.addWidget(self.select_arduino_label)
#         vbox_device.addWidget(self.select_arduino_button)

#         ports = list_resources()

#         self.select_arduino_button.addItems(ports)

#         # adds another button to the vertical layout that starts the scan

#         self.scan_label = QtWidgets.QLabel(" ")
#         self.scan_button = QtWidgets.QPushButton("Click to Start Scan")

#         vbox.addWidget(self.scan_label)
#         vbox.addWidget(self.scan_button)

#         self.scan_button.clicked.connect(self.plot)

#     def getSaveFileName(self):
#         filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
#         with open(f"{filename}", "w", newline="") as csvfile:
#             write = csv.writer(csvfile)

#             write.writerow(
#                 [
#                     "adc value",
#                     "Average Voltage (u)",
#                     " Average Current (I)",
#                     " Error on voltage",
#                     " Error on current",
#                 ]
#             )
#             for adc, u, i, eu, ei in zip(
#                 self.list_adc,
#                 self.list_averages_U,
#                 self.list_averages_I,
#                 self.list_standard_error_U,
#                 self.list_standard_error_I,
#             ):
#                 write.writerow([adc, u, i, eu, ei])

#         print(filename)

#     def plot(self):
#         """Clear the plot widget and display experimental data."""

#         # this clears it so if we want to scan multiple times, it womn't overlap
#         self.plot_widget.clear()

#         start = int(self.start_button.value())
#         end = int(self.end_button.value())
#         number = self.number_button.value()

#         # port="ASRL10::INSTR"
#         diode = DiodeExperiment(port=self.select_arduino_button.currentText())
#         (
#             self.list_averages_U,
#             self.list_standard_error_U,
#             self.list_averages_I,
#             self.list_standard_error_I,
#             self.list_adc,
#         ) = diode.scan(start, end, number)

#         # Genereer wat data als demo.
#         # **Let op:** `x`, `y`, `x_err` en `y_err` *moeten* NumPy arrays zijn *of*,
#         # en dat geldt alleen voor de errors, een vast getal.
#         x = np.array(self.list_averages_U)
#         y = np.array(self.list_averages_I)
#         x_err = np.array(self.list_standard_error_U)
#         y_err = np.array(self.list_standard_error_I)

#         # Maak eerst een scatterplot
#         self.plot_widget.plot(x, y, symbol="o", symbolSize=5, pen=None)
