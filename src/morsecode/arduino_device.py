"""This module is the controller of an arduino.
You can see all available ports and check the identification string.
You can both set and find out the output value on the LED.
With each output voltage the output value and voltage on the LED can be measured.
"""

import pyvisa

rm = pyvisa.ResourceManager("@py")


def list_resources():
    """returns list of available ports

    Returns:
    ports (tuple): all available ports
    """

    return rm.list_resources()


class ArduinoVISADevice:

    def __init__(self, port):
        """running the controller of the arduino

        Args:
            port (string): port the arduino is located in
        """

        self.device = rm.open_resource(
            f"{port}", read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        """return identification string of connected device

        Returns:
            string: identification string of the arduino
        """

        return self.device.query(f"*IDN?")

    def set_output_value(self, value):
        """set a value on the output channel

        Args:
            value (integer): output value for arduino
        """
        self.device.query(f"OUT:CH0 {value}")

    def get_input_value(self, channel):
        """get input value from input channel

        Args:
            channel (integer): the channel you want to get the input value from

        Returns:
            float: the input value of given channel
        """
        input_value = float(self.device.query(f"MEAS:CH{channel}?"))

        return input_value

    def get_input_voltage(self, channel):
        """get input value from input channel in Volt

        Args:
            channel (integer): the channel you want to get the input voltage from

        Returns:
            float: the voltage on the given channel
        """
        ch_value = float(self.get_input_value(channel))
        input_voltage = ch_value * (3.3 / 1024)

        return input_voltage

    def get_output_value(self):
        """get the value of the output channel

        Returns:
            integer: the value of the output channel
        """
        output_value = float(self.device.query(f"OUT:CH0?"))

        return output_value
    
    def close(self):
        """Closes the arduino
        """
        self.device.close()