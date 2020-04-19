import ctypes
import time
from pynput.mouse import Listener

def turnRight():
    ctypes.windll.user32.mouse_event(0x0001 , 1500, 0, 0, 0)
    ctypes.windll.user32.mouse_event(0x0001 , 1500, 0, 0, 0)

def turnLeft():
    ctypes.windll.user32.mouse_event(0x0001 , -1500, 0, 0, 0)
    ctypes.windll.user32.mouse_event(0x0001 , -1500, 0, 0, 0)

def lookUp():
    ctypes.windll.user32.mouse_event(0x0001 , 0, -1500, 0, 0)

def lookDown():
    ctypes.windll.user32.mouse_event(0x0001 , 0, 1500, 0, 0)