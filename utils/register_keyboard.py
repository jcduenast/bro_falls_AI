# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys


if __name__ == '__main__':
    ti = time.time()
    time_list = []
    for i in range(2000):
        ti = time.time()
        keys = key_check()
        tf = time.time() - ti
        print( 'time:', tf, 'keys:', keys)
        time_list.append(tf)

'''
import win32api
pip install pywin32==301
pip install pypiwin32
'''
