import time

import numpy as np
import pyvisa

from morsecode.arduino_device import ArduinoVISADevice

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


class MorseCode:
    """A class that runs the diode experiment"""

    def __init__(self, port):
        """running the controller of the arduino.

        Args:
            port (string): port the arduino is located in
        """
        # running the controller of the arduino
        self.device = ArduinoVISADevice(port)

    def get_identification(self):
        """return identification string of connected device

        Returns:
            string: identification string of the arduino
        """

        return self.device.get_identification()

    def send_message(self, string):
        letters = list(string)

        for letter in letters:

            item = MORSE_CODE_DICT[f"{letter}"]

            signals_string = list(item)

            for signal in signals_string:

                if signal == ".":
                    self.device.set_output_value(1023)
                    time.sleep(0.5)
                    self.device.set_output_value(0)
                    time.sleep(0.5)

                if signal == "-":
                    self.device.set_output_value(1023)
                    time.sleep(2)
                    self.device.set_output_value(0)
                    time.sleep(0.5)

    def close(self):
        """Closes the arduino"""
        self.device.close()
