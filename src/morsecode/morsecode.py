import numpy as np
import pyvisa

from morsecode.arduino_device import ArduinoVISADevice, list_resources

rm = pyvisa.ResourceManager("@py")

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def list_resources():
    """returns list of available ports

    Returns:
    ports (tuple): all available ports
    """

    ports = rm.list_resources()

    return ports

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
        
    
    def close(self):
        """Closes the arduino
        """
        self.device.close()
