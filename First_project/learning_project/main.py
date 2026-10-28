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
tuch_switch = TouchSensor(Port.S2)
end_color = ColorSensor(Port.S4)

gyro_sensor = GyroSensor(Port.S3, Direction.CLOCKWISE)
rotate_in = DataLog("rotation", name = "rotation", timestamp = False, extension = "csv", append = True)

# Write your program here.
ev3.speaker.beep()
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=92)
robot.turn(-180)
gyro_sensor.reset_angle(0)
while True:
    if end_color.color() == Color.RED:
        break
    
    #if end_color.color() == Color.BLUE:
        ev3.speaker.beep(frequency=1000, duration=500)
        wait(60)
        break
        ev3.speaker.beep(frequency=1000, duration=500)
    #if end_color.color() == Color.GREEN:
    
        ev3.speaker.beep(frequency=1000, duration=500)
        wait(60)
        ev3.speaker.beep(frequency=1000, duration=500)
        wait(60)
        break
    robot.drive(-200,0)
    if tuch_switch.pressed():
        robot.drive(200,0)
        robot.turn(180)
        wait(10)
        rotate_in.log(gyro_sensor.angle())

    if obstacle_sensor.distance() > 300:
        robot.drive(0,0)
        robot.turn(-180)
        robot.drive(200,0)

    

ev3.speaker.beep(frequency=1000, duration=500)
