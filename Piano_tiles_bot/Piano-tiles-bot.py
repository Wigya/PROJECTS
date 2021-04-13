import win32api, win32con
import time
from PIL import ImageGrab


def left_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)


while True:
    if ImageGrab.grab().getpixel((600, 576)) == (0, 0, 0):
        left_click(600, 576)
        print('clicked 1ND TILE')
    if ImageGrab.grab().getpixel((699, 565)) == (0, 0, 0):
        left_click(699, 565)
        print('clicked 2ST TILE')
    if ImageGrab.grab().getpixel((795, 558)) == (0, 0, 0):
        left_click(795, 558)
        print('clicked 3RD TILE')
    if ImageGrab.grab().getpixel((886, 555)) == (0, 0, 0):
        left_click(886, 555)
        print('clicked 4TH TILE')
