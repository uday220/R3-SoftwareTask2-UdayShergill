import socket
import pynput
from pynput import keyboard
TCP_IP = '127.0.0.1'
TCP_PORT = 2003
BUFFER_SIZE = 2048321
def on_press(key):
    motor1 = "f"
    motor2 = "f"
    motor3 = "f"
    motor4 = "f"
    speed = "255"
    if key.char == 'w':
        motor1 = "f"
        motor2 = "f"
        motor3 = "f"
        motor4 = "f"
    if key.char == 'a':
        motor1 = "r"
        motor2 = "r"
        motor3 = "f"
        motor4 = "f" 
    if key.char == 'd':
        motor1 = "f"
        motor2 = "f"
        motor3 = "r"
        motor4 = "r" 
    if key.char == 's':
        motor1 = "r"
        motor2 = "r"
        motor3 = "r"
        motor4 = "r" 
    if key.char == '5':
        speed = "255"
    if key.char == '4':
        speed = "204"
    if key.char == '3':
        speed = "153"
    if key.char == '2':
        speed = "102"
    if key.char == '1':
        speed = "51"
    if key.char == '0':
        speed = "0"
    output = ("[{}{}][{}{}][{}{}][{}{}]".format(motor1,speed,motor2,speed,motor3,speed,motor4,speed))
    output = bytes(str(output), "ascii")
    MESSAGE = output
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    s.recv(1024)
    s.close()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()