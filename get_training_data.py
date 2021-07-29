from utils.screen_capture import grab_screen
from utils.register_keyboard import key_check
import cv2
import numpy as np
import time
import os
import pickle

# def create_folder(path):
#     try:
#         # os.mkdir(path)
#         os.makedirs(path)
#         print("Directory ", path, " Created ")
#     except FileExistsError:
#         print("Directory ", path, " already exists")

key_pressed = []
ti = time.time()
# tf_list = []

running = True
capture = False

data = []

while running:
    key_pressed = key_check()
    if capture:
        frame = grab_screen([0, 30, 1024, 768])
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame_canny = cv2.Canny(frame_gray, 100, 200)
        data.append((key_pressed, frame_gray))
        if 'H' in key_pressed:
            capture = False
            print('Capture OFF')
    else:
        if 'G' in key_pressed:
            capture = True
            print('Capture ON')
    if 'J' in key_pressed:
        running = False

with open('../bro_falls_AI_data/training/data.pickle', 'wb') as f:
    pickle.dump(data, f)

cv2.imshow('color', frame)
cv2.imshow('gray', frame_gray)
cv2.imshow('canny', frame_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()



# for i in range(2000):
#     frame = grab_screen([0, 30, 1024, 768])
#     key_pressed = key_check()
#     tf = time.time() - ti
#     print('FPS', 1/tf, 'keys', key_pressed)
#     # tf_list.append(tf)
#     ti = time.time()

# print('Avg FPS', 1/np.mean(tf_list))  #Avg FPS 60.1404