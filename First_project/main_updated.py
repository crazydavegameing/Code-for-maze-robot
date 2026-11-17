#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.C)
obstacle_sensor = UltrasonicSensor(Port.S1)
kill_switch = TouchSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

while not kill_switch.pressed():
    ev3.speaker.beep(frequency=1000, duration=200)

    robot.drive(200, 0)

    while obstacle_sensor.distance() > 300 and not kill_switch.pressed():
        wait(10)

    if kill_switch.pressed():
        break

    robot.straight(-300)
    robot.turn(120)
