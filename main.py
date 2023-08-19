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
text = "подключен yfinance введите название данных акций"
def read_speak(text):
    speak.Speak(text)

while True:
    read_speak(text)
    read_speak("создаю временные ряды")
    inn = input(">>>")
    in_data_co = yf.download(inn,start="2014-01-01",end= str(time.strftime("%Y-%m-%d")),interval = "1d")

    for i in range(1):
        time.sleep(1)

        data_time = str(time.time())

        data_filter_close = in_data_co.filter(["Close"])
        plt.plot(data_filter_close)
        plt.savefig(str(inn) + ".png")
        plt.show()
        data_pandas = pd.DataFrame(np.array(in_data_co["Close"]))

        #print(np.array([i,data_time]))
        #print(data_pandas)
        data_pandas.to_csv(str(inn) + ".csv")
        if i == 0:
            print(i)
            print(data_filter_close["Close"][-1])
            read_speak(str(int(data_filter_close["Close"][-1])))
            read_speak(str(inn))
            read_speak("Анализ данных")
            read_speak("количество строк")
            read_speak(data_filter_close.shape[0])
            read_speak("Применяю метод линейной регрессии для прогнозирования")
            print(data_filter_close)


            read_speak("закрываю программу")
            exit()
