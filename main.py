# -*- coding: utf-8 -*-
name = None
row_status = None
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
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
    in_data_co = yf.download(input(">>>"),start="2014-01-01",end= str(time.strftime("%Y-%m-%d")),interval = "1d")

    for i in range(1):
        time.sleep(1)

        data_time = str(time.time())

        data_filter_close = in_data_co.filter(["Close"])
        plt.plot(data_filter_close)
        plt.savefig(str(time.time()) + ".png")
        plt.show()
        data_pandas = pd.DataFrame(np.array(in_data_co["Close"]))

        #print(np.array([i,data_time]))
        #print(data_pandas)
        data_pandas.to_csv("test.csv")
        if i == 0:
            print(i)
            print(data_filter_close["Close"][0])
            read_speak(str(int(data_filter_close["Close"][0])))
            read_speak("закрываю программу")
            exit()
