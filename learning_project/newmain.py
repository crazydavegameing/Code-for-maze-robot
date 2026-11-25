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
obstacle_sensor = UltrasonicSensor(Port.S3)
touch_switch = TouchSensor(Port.S1)
end_color = ColorSensor(Port.S2)
gyro_sensor = GyroSensor(Port.S4, Direction.CLOCKWISE)
x = gyro_sensor.angle()
last_turn = False
rotate_in = DataLog("rotation", name = "rotation", timestamp = False, extension = "txt", append = True)
# Write your program here.
ev3.speaker.beep()
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=92)
#robot.turn(-220)
gyro_sensor.reset_angle(0)


def sensor_turn(clearance, turn_angle, last):    
    robot.drive(clearance,0)
    wait(3000)
    gyro_sensor.reset_angle(0)
    while(gyro_sensor.angle() > -84.5):
        robot.drive(0,-100)
        wait(10)
    robot.stop()
    gyro_sensor.reset_angle(0)

    


def tuch_sensor(clearance, turn_angle):
    if touch_switch.pressed():
        ev3.speaker.beep()
        robot.drive(clearance,0)
        wait(800)
        gyro_sensor.reset_angle(0)
        while(gyro_sensor.angle() < 84):
            robot.drive(0,100)
            wait(10)
        robot.stop()
        gyro_sensor.reset_angle(0)



def moveInALine():
    gyro_sensor.reset_angle(0)
    x = gyro_sensor.angle()
    robot.drive(-100, x)


while True:
    if end_color.color() == Color.RED:
        break
    #if end_color.color() == Color.BLUE:
        ev3.speaker.beep(frequency=1000, duration=500)
        wait(60)
        ev3.speaker.beep(frequency=1000, duration=500)
    #if end_color.color() == Color.GREEN:
        ev3.speaker.beep(frequency=1000, duration=500)
        wait(60)
        ev3.speaker.beep(frequency=1000, duration=500)
    moveInALine()
    tuch_sensor(100, 170)
    if obstacle_sensor.distance() > 450 and last_turn == True:
        last_turn = False
        sensor_turn(-100, -170, last_turn)
        ev3.speaker.beep()
    elif obstacle_sensor.distance() < 450:
        last_turn = True
        




    

ev3.speaker.beep(frequency=1000, duration=500)
