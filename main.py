# -*- coding: utf-8 -*-
name = None
row_status = None
import numpy as np
import pandas as pd
import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Rate = 3
speak.Volume = 100

text = "бот активирован"
speak.Speak(text)
