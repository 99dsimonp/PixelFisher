import cv2 as cv
import numpy as np
import mss
import pyautogui
import time
import pyaudio
import struct
import math
import random

sct = mss.mss()
all = sct.monitors

found_fish = False
p = pyaudio.PyAudio()
SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2
Max_Seconds = 15
TimeoutSignal=((RATE / chunk * Max_Seconds) + 2)
Time=0
Threshold = 90
#assert(p.get_default_input_device_info()['name'] == 'CABLE Output (VB-Audio Virtual ')
print(p.get_default_input_device_info()['name'])
print(p.get_default_output_device_info()['name'])
#FIND INDEX OF YOUR VIRTUAL DEVICE AND INPUT IN FOLLOWING STATEMENT
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = chunk)#,
                #input_device_index= 18,
                #output_device_index = 13)

def rms(frame):
    count = len(frame)/swidth
    format = "%dh"%(count)
    # short is 16 bit int
    shorts = struct.unpack(format, frame)

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n
    # compute the rms
    rms = math.pow(sum_squares/count,0.5);
    return rms * 1000

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
        pyautogui.moveTo(mid)

        while True:
            try:
                input = stream.read(chunk)
            except:
                continue
            rms_value = rms(input)
            print(rms_value)
            if found_fish and rms_value < Threshold:
                found_fish = False

            if not found_fish and rms_value > Threshold:
                print("Bobber splash")
                time.sleep(0.150 + random.random())
                pyautogui.rightClick()
                time.sleep(1 + random.random())
                found_fish = True
                break
            if Time > TimeoutSignal:
                print("Timed out, no bobber heard")
                break
            Time = Time + 1
        Time = 0
        #p.close(stream)