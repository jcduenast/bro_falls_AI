import pickle
import numpy as np
import cv2

with open('../bro_falls_AI_data/training/data.pickle', 'rb') as f:
    data = pickle.load(f)

print(data[0][0])
print(type(data[0][1]))
cv2.imshow('np image', data[0][1])
cv2.waitKey(0)
cv2.destroyAllWindows()
