from vex import (
    Brain, Motor, Ports, Colorsensor, Sonar, Bumper, ColorHue, BrakeType,
    DEGREES, FORWARD, PERCENT, SECONDS, REVERSE, MM, BrainLcd
)
import sys
import vex

# INITIALIZATION OF ROBOT PARTS
# ==========================

# brain initialization
brain = Brain()

# motors initialization
right_motor = Motor(Ports.PORT12)
left_motor = Motor(Ports.PORT1)
arm_motor = Motor(Ports.PORT10)
claw_motor = Motor(Ports.PORT4)

# sensors initialization
sonar_sensor = Sonar(Ports.PORT8)
color_sensor = Colorsensor(Ports.PORT6, False)
lcd = BrainLcd()

# Task 1 - for 1st and 2nd member
def rectangle():
    while True:
        left_motor.spin(REVERSE, 60, PERCENT)
        right_motor.spin(FORWARD, 60, PERCENT)
        vex.wait(2)

        left_motor.spin(REVERSE, 40, PERCENT)
        right_motor.spin(FORWARD, 0, PERCENT)
        vex.wait(2)