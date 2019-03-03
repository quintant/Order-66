import os
import time
from pynput import keyboard


def order_66():
    os.system("TASKKILL /F /IM bfv.exe")
    os.system('cls')
    print("BFV.EXE er dead now :'( ")
    time.sleep(4)


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.ctrl_r:
        order_66()
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
