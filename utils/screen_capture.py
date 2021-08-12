import cv2
# import pyautogui
# from PIL import ImageGrab
import time
import numpy as np
import imageio

import win32gui, win32ui, win32con, win32api  # sentdex


def grab_screen(region=None):  # From sentdex GTA V Python project
    hwin = win32gui.GetDesktopWindow()
    if region:
            left,top,x2,y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)


def get_frame(roi):
    # image = pyautogui.screenshot(region=(roi[0], roi[1], roi[0]+roi[2], roi[1]+roi[3]))  # Avg Menu 28.8684 fps
    # image = ImageGrab.grab(bbox=(roi[0], roi[1], roi[0]+roi[2], roi[1]+roi[3]))  # Avg Menu 27.6566 fps
    image = grab_screen(roi)  # Avg Menu 60.2323 fps
    return image


if __name__ == '__main__':
    ti = time.time()
    time_list = []
    for i in range(200):
        ti = time.time()
        frame = np.array(get_frame([0, 30, 320, 240]))
        # cv2.imshow('desktop cutout', cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR))
        tf = time.time() - ti
        print('Frequens:', 1/tf, 'time:', tf)
        time_list.append(tf)

    print('Average frequens:', 1/np.mean(time_list))

    cv2.imshow('Frame example', frame)
    cv2.waitKey(0)

