#!/usr/bin/env pybricks-micropython 
# main.py 
import socket 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor 
from pybricks.parameters import Port 
from pybricks.robotics import DriveBase 

# Initialize EV3 components 
ev3 = EV3Brick() 
claw_motor = Motor(Port.B)

# Server configuration 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(("0.0.0.0", 12345)) 
server_socket.listen(1)
print("Waiting for connection ... ") 
client_socket, address = server_socket.accept() 
print("Connected to {}".format(address))


try: 
    while True:
         command = client_socket. recv(2). decode() 
         if not command: 
            break
         key, action = command[0], command [1] 
         if action=="d": # Key press 
            if key=="a": 
                claw_moter.run(30) 
            elif key=="s": 
                claw_moter.run(30) 
         elif action=="u": # Key release
            if key in ("a", "s", "d"):
                 robot. stop() # Stop the robot on key release 
finally: 
    client_socket.close() 
    server_socket.close()
