# get the coords of a point when clicking with pynput

import pynput
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        print(f'x: {x}, y: {y}')

with Listener(on_click=on_click) as listener:
    listener.join()

