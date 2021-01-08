from pyautogui import *
from pynput.keyboard import Key, Controller
import time
import win32api
import win32con
from python_imagesearch.imagesearch import *
import os

keyboard = Controller()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def starzoom():
    os.startfile("C:/Users/27tj/AppData/Roaming/Zoom/bin/Zoom.exe")


def quitzoom():
    os.system("TASKKILL /F /IM Zoom.exe")


def join(_id_, pwd):
    starzoom()
    time.sleep(2)
    pos_0 = imagesearch("zoom_join_meeting.png")
    if pos_0[0] != -1:
        print("position : ", pos_0[0], pos_0[1])
        click(pos_0[0], pos_0[1])
        time.sleep(2)
        pos_1 = imagesearch("zoom_id.png")
        if pos_1[0] != -1:
            print("position : ", pos_1[0], pos_1[1])
            click(pos_1[0], pos_1[1])
            keyboard.type(_id_)  # meeting id
            time.sleep(2)
            pos_2 = imagesearch("zoom_join_meeting.png")
            if pos_2[0] != -1:
                print("position : ", pos_2[0], pos_2[1])
                click(pos_2[0], pos_2[1])
                time.sleep(2)
                pos_3 = imagesearch("zoom_password.png")
                if pos_3[0] != -1:
                    print("position : ", pos_3[0], pos_3[1])
                    click(pos_3[0], pos_3[1])
                    keyboard.type(pwd)  # password
                    time.sleep(2)
                    pos_4 = imagesearch("zoom_join_meeting.png")
                    if pos_4[0] != -1:
                        print("position : ", pos_4[0], pos_4[1])
                        click(pos_4[0], pos_4[1])
                    else:
                        print("image not found")
                else:
                    print("image not found")
            else:
                print("image not found")
        else:
            print("image not found")
    else:
        print("image not found")


def lesson(tstart: [str], tend: [str], id_, pwd):
    t = time.strftime("%H:%M:%S", time.gmtime())
    while t <= tstart:
        t = time.strftime("%H:%M:%S", time.gmtime())
        print(t)
        time.sleep(1)
    if tstart <= t <= tend:
        join(id_, pwd)
        while not t >= tend:
            t = time.strftime("%H:%M:%S", time.gmtime())
            if t >= tend:
                quitzoom()
                print("lesson end")
            else:
                print(t)
                time.sleep(1)
