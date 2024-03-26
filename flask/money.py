import numpy as np
import pandas as pd
from FinMind.data import DataLoader
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf


pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", 180)


def getDataYF(prod, st, en):
    tmpdata = yf.download(prod, start=st, end=en)
    tmpdata.columns = [i.lower() for i in tmpdata.columns]
    return tmpdata


def ChartCandle(data, addp=[]):
    mcolor = mpf.make_marketcolors(up="r", down="g", inherit=True)
    mstyle = mpf.make_mpf_style(base_mpf_style="yahoo", marketcolors=mcolor)
    mpf.plot(data, addplot=addp, type="candle", style=mstyle, volume=True)


# from money import getDataYF
# data=getDataYF('4906.tw','2023-07-01','2023-08-19')
# print(data)

from money import ChartCandle

data1 = getDataYF("4906.tw", "2023-07-01", "2023-08-19")
data1["ceil"] = data1.rolling(3)["high"].max().shift()
position = 0
trade = pd.DataFrame()
for i in range(data1.shape[0] - 1):
    c_time = data1.index[i]
    c_close = data1.loc[c_time, "high"]
    c_ceil = data1.loc[c_time, "close"]
    n_time = data1.index[i + 1]
    n_open = data1.loc[n_time, "open"]
    if position == 0:
        if c_close > c_ceil:
            position = 1
            order_i = i
            order_time = n_time
            order_price = n_open
            order_unit = 1
    elif position == 1:
        if c_high < c_ceil:
            position = 0
            cover_time = n_time
            cover_price = n_open
            trade = trade.append(pd.Series([]))


ChartCandle(data1)
