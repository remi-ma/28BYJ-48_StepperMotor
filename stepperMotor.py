##############################################################################################
# Project     : 28BYJ-48 Stepper Motor driver
# File        : stepperMotor.py
# Author      : remi-ma
# Date        : 27/02/18
# Description : Control 28BYJ-48 Stepper Motor for Raspberry Pi
# License     : None
##############################################################################################

import time
import RPi.GPIO as GPIO
import numpy as np

REVOLUTION_STEP_NUMBER = 2048

GPIO_PIN_LIST = [17, 27, 23, 24]


def init_gpio(pinlist):
    """
    Initialize GPIO.

    :param pinlist: GPIO list. Order is important...
    :return: None
    """
    GPIO.setmode(GPIO.BCM)
    for pin in pinlist:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)


class StepperMotor(object):
    def __init__(self, gpio_pin_list):
        """
        Initialize GPIO and Step Motor status.

        :param gpio_pin_list: GPIO list
        """
        self.gpio_list = gpio_pin_list
        init_gpio(self.gpio_list)
        self.phase = [1, 1, 0, 0]

    def get_phase(self):
        """
        Get the phase of the 4 phases Stepper motor.

        :return: phase of step motor
        """
        return self.phase

    def rotate_segment(self, direction=True):
        """
        Perform one step.

        :param direction: (Boolean) Clockwise = True | Inverted = False
        :return: None
        """
        if direction:
            self.phase = np.roll(self.phase, 1)
        else:
            self.phase = np.roll(self.phase, -1)

        for pin_idx in range(len(self.gpio_list)):
            GPIO.output(self.gpio_list[pin_idx], int(self.phase.astype(int)[pin_idx]))

    def rotate(self, direction, degrees=0):
        """
        Perform rotation with direction and angle info.

        :param direction: (Boolean) Clockwise = True | Inverted = False
        :param degrees: angle of rotation
        :return: None
        """
        step_number = int(REVOLUTION_STEP_NUMBER * degrees / 360)
        for i in range(0, step_number):
            self.rotate_segment(direction=direction)
            time.sleep(.002)


if __name__ == '__main__':
    try:
        motor = StepperMotor(GPIO_PIN_LIST)
        motor.rotate(direction=True, degrees=180)
        motor.rotate(direction=False, degrees=360)
        motor.rotate(direction=True, degrees=90)
        motor.rotate(direction=False, degrees=45)

    except KeyboardInterrupt:
        GPIO.cleanup()

    finally:
        GPIO.cleanup()
        print("Finished")

