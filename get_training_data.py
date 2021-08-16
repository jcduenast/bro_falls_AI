import numpy

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

training_data_path = '../bro_falls_AI_data/training/'
data_id = 0
key_pressed = []
running = True
capture = False
data_img = []
data_input = []

### store images as png
save_png = True
frame_counter = 0

# Print operation info
print("Press 'G' to start recording.\nPress 'H' to stop.\nPress 'J' to end the program ")

while running:
    key_pressed = key_check()
    if capture:
        frame = grab_screen([960-400, 550-300, 960+400, 550+300]) #grab_screen([0, 30, 1024, 768])
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # frame_canny = cv2.Canny(frame_gray, 100, 200)
        data_img.append(frame_gray)
        data_input.append(key_pressed)
        if save_png:
            cv2.imwrite(training_data_path+'/data_{:0>4}/f_{:0>4}.png'.format(data_id, frame_counter), frame_gray)
            frame_counter += 1

        if 'H' in key_pressed:
            capture = False
            print('Capture OFF')
            while os.path.exists(training_data_path+'data_{:0>4}_input.pickle'.format(data_id)):
                data_id += 1
            with open(training_data_path+'data_{:0>4}_input.pickle'.format(data_id), 'wb') as f:
                pickle.dump(data_input, f)
            np.save(training_data_path+'data_{:0>4}_img'.format(data_id), np.array(data_img))
            print('data_{:0>4} saved'.format(data_id))
    else:
        if 'G' in key_pressed:
            if save_png:
                while os.path.isdir('../bro_falls_AI_data/training/data_{:0>4}'.format(data_id)) or \
                        os.path.exists(training_data_path+'data_{:0>4}_input.pickle'.format(data_id)):
                    data_id += 1
                os.makedirs('../bro_falls_AI_data/training/data_{:0>4}'.format(data_id))
            capture = True
            frame_counter = 0
            print('Capture ON')
    if 'J' in key_pressed:
        if capture:
            capture = False
            print('Capture OFF')
            while os.path.exists(training_data_path + 'data_{:0>4}_input.pickle'.format(data_id)):
                data_id += 1
            with open(training_data_path + 'data_{:0>4}_input.pickle'.format(data_id), 'wb') as f:
                pickle.dump(data_input, f)
            np.save(training_data_path + 'data_{:0>4}_img'.format(data_id), np.array(data_img))
            print('data_{:0>4} saved'.format(data_id))
        running = False

# with open(training_data_path+'data_{:0>4}.pickle'.format(data_id), 'wb') as f:
#     pickle.dump(data, f)
#
# cv2.imshow('color', frame)
# cv2.imshow('gray', frame_gray)
# cv2.imshow('canny', frame_canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# ti = time.time()
# for i in range(2000):
#     frame = grab_screen([0, 30, 1024, 768])
#     key_pressed = key_check()
#     tf = time.time() - ti
#     print('FPS', 1/tf, 'keys', key_pressed)
#     # tf_list.append(tf)
#     ti = time.time()

# print('Avg FPS', 1/np.mean(tf_list))  #Avg FPS 60.1404