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
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "h": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
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
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": ":",
}

LETTERS_DICT = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "h",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    "--..--": ",",
    ".-.-.-": ".",
    "..--..": "?",
    "-..-.": "/",
    "-....-": "-",
    "-.--.": "(",
    "-.--.-": ")",
    ":": " ",
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
        print(letters)

        for letter in letters:

            item = MORSE_CODE_DICT[f"{letter}"]

            signals_string = list(item)
            print(signals_string)

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

                if signal == ":":
                    time.sleep(4)

            time.sleep(2)

    def receive_message(self):
        self.letters = {}
        self.code = []

        for i in range(1, 100):
            time.sleep(0.1)

            value = self.device.get_input_value(2)

            start_time = time.time()

            if value >= 60:
                # calculating time LED is off
                temp_time = time.time()
                total_time_off = temp_time - start_time

                # time measurement is started
                start_time = time.time()

                # getting code list
                if total_time_off > 1 and total_time_off <= 2:
                    if value <= 60:
                        end_time = time.time()

                        total_time_on = end_time - start_time

                        if total_time_on > 0.25 and total_time_on <= 2:
                            symbol = "."

                        if total_time_on > 1.5 and total_time_on <= 4:
                            symbol = "-"

                    self.code.append(symbol)

                # when new letter, code list is converted to string and the letter is added to letters list
                if total_time_off > 1.5 and total_time_off < 2.5:
                    self.letter = "".join(self.code)

                    self.letters.append(self.letter)

                # when space, a space symbol is added to letters list
                if total_time_off > 3.5 and total_time_off <= 4.5:
                    symbol = ":"

                    self.letters.append(symbol)

                # when time is longer than 5, end measurement
                if total_time_off > 10:
                    text = []

                    for letter in self.letters:
                        real_letter = LETTERS_DICT[f"{letter}"]
                        text.append(real_letter)

                    self.string = "".join(text)

        return self.string

    # def receive():
    #     for symbol in code:
    #     item = LETTERS_DICT{f"{code}"}

    def close(self):
        """Closes the arduino"""
        self.device.close()
