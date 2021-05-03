import cv2 as cv
import numpy as np
import mss
import pyautogui
import time
import random

sct = mss.mss()
all = sct.monitors
Timeout = 5000
Time = 0

while True:
    pyautogui.press('1')
    random_time = random.random()
    time.sleep(2.7 + random_time)
    scr2 = sct.grab({"mon": 2, "top": 0,"left": 0, "width": 2560, "height": 1440})
    img = np.array(scr2)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    if cv.waitKey(25) & 0xFF == ord("x"):
        break

    template = cv.imread('bobber.jpg', 0)
    w, h = template.shape[::-1]
    methods = ['cv.TM_CCOEFF_NORMED']#, 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    for meth in methods:
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum, else take max
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        mid = (top_left[0] + w/2, top_left[1] + h/2)
        mid_moveto = (mid[0] + random.randint(0, 5), mid[1] + random.randint(0,5))
        pyautogui.moveTo(mid_moveto)

        while True:
            new_screen = sct.grab({"mon": 2, "top": 0,"left": 0, "width": 2560, "height": 1440})
            img2 = np.array(new_screen)
            img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
            bobber_match = cv.matchTemplate(img2,template,method)
            min_val2, max_val2, min_loc2, max_loc2 = cv.minMaxLoc(bobber_match)
            top_left2 = max_loc2
            new_mid = (top_left2[0] + w/2, top_left2[1] + h/2)
            #Print diff in center location. If script doesnt click when bobber splashes you can change the value below to be smaller or larger.
            print(abs(new_mid[0] - mid[0]) + abs(new_mid[1] - mid[1]))
            if abs(new_mid[0] - mid[0]) + abs(new_mid[1] - mid[1]) > 13:
                print("Bobber splash")
                time.sleep(0.150 + random.random()+random.random())
                pyautogui.rightClick()
                time.sleep(1 + random.random())
                found_fish = True
                break
            if Time > Timeout:
                print("Timed out, no bobber heard")
                break
            Time = Time + 1
    Time = 0