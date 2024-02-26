import pyautogui
from pynput import keyboard
import time


stop_program = False


def move_mouse(x, y, duration=0.25):
    pyautogui.moveRel(x, y, duration=duration)


def on_press(key):
    global stop_program
    if key == keyboard.Key.esc:
        stop_program = True


listener = keyboard.Listener(on_press=on_press)
listener.start()


def main():
    while not stop_program:
        move_mouse(50, 0)
        if stop_program:
            break        
        move_mouse(0, 50)
        if stop_program:
            break       
        move_mouse(-50, 0)
        if stop_program:
            break        
        move_mouse(0, -50)
        if stop_program:
            break

if __name__ == "__main__":
    main()

