# -*- coding: utf-8 -*-
name = None
row_status = None
import os
import math
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from tensorflow.keras.models import save_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
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
        data_filter_volume = in_data_co.filter(["Volume"])
        plt.plot(data_filter_close)
        plt.savefig("image/" + str(inn) + ".png")
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
            no = "отклонено"
            read_speak(no)
            print(data_filter_close)

            # Запуск нейронки
            text_neiro = "Запуск нейронки краткосрочной и долгосрочной памяти LSTM DENSE"
            read_speak(text_neiro)

            start_time = time.time()

            data_read_pandas_BTC_RUB = pd.DataFrame(data_filter_close)
            text_neiro = "Проверяем данные"
            read_speak(text_neiro)
            print(data_read_pandas_BTC_RUB)
            pdata = data_read_pandas_BTC_RUB
            print(pdata)
            data_read_pandas_BTC_RUB = data_read_pandas_BTC_RUB.tail(2000)
            data_read_pandas_BTC_RUB_shape_row, data_read_pandas_BTC_RUB_shape_col = data_read_pandas_BTC_RUB.shape[0], \
                                                                                   data_read_pandas_BTC_RUB.shape[1]
            print(data_read_pandas_BTC_RUB.shape)
            print([data_read_pandas_BTC_RUB_shape_row, data_read_pandas_BTC_RUB_shape_col])

            filter_BTC_RUB_price = data_read_pandas_BTC_RUB.filter(["Close"])

            print(filter_BTC_RUB_price)

            # create dATEFRAME CLOSE
            data = data_read_pandas_BTC_RUB.filter(["Close"])

            # data_df_pandas_filter = data_df_pandas.filter(["Well"])
            print(data)

            # convert dataframe
            dataset = data.values
            text_neiro = "Делаем датасет"
            read_speak(text_neiro)
            # dataset  = data_df_pandas_filter.values
            print(dataset)

            text_neiro = "Создаем тренировочные данные"
            read_speak(text_neiro)

            # get the number rows to train the model
            training_data_len = math.ceil(len(dataset) * .8)
            print(training_data_len)

            text_neiro = "Приводим в машиночитаемые данные"
            read_speak(text_neiro)

            # scale the data
            scaler = MinMaxScaler(feature_range=(0, 1))
            scaled_data = scaler.fit_transform(dataset)
            print(scaled_data)

            text_neiro = "Сохраняем график в файл"
            read_speak(text_neiro)

            plt.plot(scaled_data)
            plt.savefig("scaled_data_BTC_RUB.png")

            text_neiro = "Создаем тренировочный датасет"
            read_speak(text_neiro)
            # create the training dataset
            train_data = scaled_data[0:training_data_len, :]
            # split the data into x_train and y_train data sets
            x_train = []
            y_train = []
            for rar in range(60, len(train_data)):
                x_train.append(train_data[rar - 60:rar, 0])
                y_train.append(train_data[rar, 0])
                if rar <= 61:
                    print(x_train)
                    print(y_train)
                    print()

            text_neiro = "Конвертируем тренировочный датасет"
            read_speak(text_neiro)
            # conver the x_train and y_train to numpy arrays
            x_train, y_train = np.array(x_train), np.array(y_train)
            # reshape the data
            x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
            print(x_train.shape)
            import tensorflow as tf

            text_neiro = "Создаем модель "
            read_speak(text_neiro)
            # biuld to LSTM model

            model = Sequential()
            model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
            model.add(LSTM(101, return_sequences=False))
            model.add(Dense(50))
            model.add(Dense(25))
            model.add(Dense(1))
            # cmopale th emodel
            model.compile(optimizer='adam', loss='mean_squared_error')
            # train_the_model
            model.summary()
            print("Fit model on training data")

            # Evaluate the model on the test data using `evaluate`
            print("Evaluate on test data")
            results = model.evaluate(x_train, y_train, batch_size=1)
            print("test loss, test acc:", results)

            text_neiro = "тренируем модель "
            read_speak(text_neiro)
            #model = tf.keras.models.load_model(os.path.join("./dnn/", "BTC_RUB_model.h5"))
            model.fit(x_train, y_train, batch_size=1, epochs=10)

            text_neiro = "сохраняем модель BTC_RUB_model.h5"
            read_speak(text_neiro)
            model.save(os.path.join("./dnn/", "BTC_RUB_model.h5"))
            # reconstructed_model = tf.keras.models.load_model(os.path.join("./dnn/", "BTC-RUB_model.h5"))

            # np.testing.assert_allclose(model.predict(x_train), reconstructed_model.predict(x_train))
            # reconstructed_model.fit(x_train, y_train)

            text_neiro = "создаем тестовый датасет"
            read_speak(text_neiro)
            # create the testing data set
            # create a new array containing scaled values from index 1713 to 2216
            test_data = scaled_data[training_data_len - 60:, :]
            # create the fata sets x_test and y_test
            x_test = []
            y_test = dataset[training_data_len:, :]
            for resr in range(60, len(test_data)):
                x_test.append(test_data[resr - 60:resr, 0])

            # conert the data to numpy array
            x_test = np.array(x_test)

            # reshape the data
            x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

            # get the model predicted price values
            predictions = model.predict(x_test)
            predictions = scaler.inverse_transform(predictions)

            text_neiro = "получаем квадрат ошибки"
            read_speak(text_neiro)
            # get the root squared error (RMSE)
            rmse = np.sqrt(np.mean(predictions - y_test) ** 2)
            print(rmse)


            # get the quate
            new_df = data_read_pandas_BTC_RUB.filter(["Close"])

            # get teh last 60 days closing price values and convert the dataframe to an array
            last_60_days = new_df[-60:].values
            # scale the data to be values beatwet 0 and 1

            last_60_days_scaled = scaler.transform(last_60_days)

            # creAte an enemy list
            X_test = []
            # Append past 60 days
            X_test.append(last_60_days_scaled)

            # convert the x tesst dataset to numpy
            X_test = np.array(X_test)

            # Reshape the dataframe
            X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
            # get predict scaled

            pred_price = model.predict(X_test)
            # undo the scaling
            pred_price = scaler.inverse_transform(pred_price)
            text_neiro = "получаем прогноз " + str(pred_price)
            read_speak(text_neiro)
            print(pred_price)

            pred_price_a = pred_price[0]
            pred_price_aa = pred_price_a[0]
            preset_pred_price = round(pred_price_aa, 6)

            print(pred_price)
            print(preset_pred_price)
            text_neiro = "получаем прогноз " + str(preset_pred_price)
            read_speak(text_neiro)
            old_time = time.time() - start_time
            print("Время на расчеты :" + str(old_time))

            time.sleep(5)

            """from sklearn.linear_model import LinearRegression

            X = np.array([data_filter_close["Close"]])
            y = np.array([data_filter_volume["Volume"]])
            reg = LinearRegression().fit(X, y)
            score = reg.score(X, y)
            coef = reg.coef_
            inter = reg.intercept_
            predict = reg.predict(np.array([X, y]))
            print(score)
            print(coef)
            print(inter)
            print(predict)"""

            read_speak("закрываю программу через минуту")
            time.sleep(60)
            exit()
