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


class MorseCodeSend:
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
            print(item)

            signals_string = list(item)
            print(signals_string)

            for signal in signals_string:
                print(signal)

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
        letter = []

        for i in range(1, 100):
            time.sleep(0.1)
            value = self.device.get_input_value(2)

            if value >= 60:
                start_time = time.time()

                if value <= 60:
                    end_time = time.time()

                    total_time = end_time - start_time

                    if total_time > 0.5 and total_time <= 2:
                        symbol = "."

                    if total_time > 2 and total_time <= 4:
                        symbol = "-"

                    if total_time > 4 and total_time <= 5:
                        symbol = ":"

                    letter.append(symbol)

        print(letter)

    # def receive(string):
    #     code = list(string)

    #     item = LETTERS_DICT[f"{}"]

    #     for

    def close(self):
        """Closes the arduino"""
        self.device.close()


# class MorseCodeReceive:
#     def __init__(self,):
#           """running the controller of the arduino.

#         Args:
#             port (string): port the arduino is located in
#         """
#         # running the controller of the arduino
#         self.device = ArduinoVISADevice(port)

#     def receive_message(self):
#         letter = []

#         for i in range(1, 100):
#             time.sleep(0.1)
#             value = self.device.get_input_value(2)

#             if value >= 60:
#                 start_time = time.time()

#                 if value <=60:
#                     end_time = time.time()

#                     total_time = end_time - start_time

#                     if total_time > 0.5 and total_time <= 2:
#                         symbol = '.'

#                     if total_time > 2 and total_time <= 4:
#                         symbol = '-'

#                     if total_time > 4 and total_time <= 5:
#                         symbol = ':'

#                     letter.append(symbol)

#         print(letter)

#     def receive(string):
#         code = list(string)

#         item = LETTERS_DICT[f"{}"]

#         for
