# -*- coding: utf-8 -*-
name = None
row_status = None
import numpy as np
import pandas as pd
import matpplotlib.pyplot as plt
import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Rate = 3
speak.Volume = 100

text = "бот активирован"

def read_speak(text):
    speak.Speak(text)

while True:
    read_speak(text)
    read_speak("создаю временные ряды")
    for i in range(10):
        time.sleep(1)
        data_time = str(time.time())
        print(np.array([i,data_time]))
        if i == 10:
            print(i)
            read_speak("закрываю программу")
            exit()
