# 28BYJ-48 StepperMotor

Python3 driver to control the 28BYJ-48 stepper motor for RaspberryPi3 platform.

## Getting Started

The main function in StepperMotor class is *rotate* : You can control the rotation of the motor with direction and angle.
* direction: Clockwise = True (default) | Inverted = False
* angle: integer in degrees, can be more than 360 for several rotations.

See example at the end of the code...

### Prerequisites

2 modules are needed to make it works:
* RPi.GPIO module to control GPIOs
* Numpy to manage list rolling for phase control.

## Authors

**remi-ma, what else... 

## What's next

For now on, you can control stepper motor with direction and angle, but we could add:
* if KeyBoardInterrupt, go back to inital position before cleaning up GPIO.
* Phase sequence can be rolled but cannot be changed... but is it useful?

