

from pynput.mouse import Button, Controller
import threading, sys, os
import time

def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        os._exit(1)
        return False




from pynput import keyboard

# Collect events until released
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

mouse = Controller()

while 1 == 1:
    mouse.click(Button.middle, 1)
    time.sleep(.2)
