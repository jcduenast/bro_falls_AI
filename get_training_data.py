from utils.screen_capture import grab_screen
from utils.register_keyboard import key_check
import cv2
import numpy as np
import time

key_pressed = []
ti = time.time()
# tf_list = []

for i in range(2000):
    frame = grab_screen([0, 30, 320, 240])
    key_pressed = key_check()
    tf = time.time() - ti
    print('FPS', 1/tf, 'keys', key_pressed)
    # tf_list.append(tf)
    ti = time.time()

# print('Avg FPS', 1/np.mean(tf_list))  #Avg FPS 60.1404