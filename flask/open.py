import urllib.request as request
import yfinance as yf
import pandas as pd
import numpy as np
import mplfinance as mpf

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", 180)



def getData(prod, st, en):
    tempData = yf.download(prod, start=st, end=en)
    tempData.columns = [i.lower() for i in tempData.columns]
    return tempData

def chartCandle(data,addp=[]):
    mcolor=mpf.make_marketcolors(up='r',down='g',inherit=True)
    mstyle=mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mcolor)
    mpf.plot(data,addplot=addp,style=mstyle,type='candle',volume=True)

from open import getData,chartCandle
mcolor=mpf.make_marketcolors(up='r',down='g',inherit=True)
mstyle=mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mcolor)


prod='3013.tw'
data = getData(prod, "2007-01-01", "2022-05-01")
print(data)
# position=0
# trade=pd.DataFrame()



# for i in range(data.shape[0]-1):
#     #取得策略會應用到的變數
#     c_time=data.index[i]
#     c_low=data.loc[c_time,'low']
#     c_high=data.loc[c_time,'high']
#     c_close=data.loc[c_time,'close']
#     c_open=data.loc[c_time,'open']
#     n_time=data.index[i+1]
#     n_open=data.loc[n_time,'open']
#     #進場程序
#     if position==0:
#         if c_close>c_open and (c_close-c_open)*2<(c_open-c_low):
#             position=1
#             order_i=i
#             order_time=n_time
#             order_price=n_open
#             order_unit=1
#             # print(c_time,'觸發進場訊號，隔日進場',order_time,'進場價',order_price,'進場',order_unit,'單位')
#         elif position == 1:
#             #出場邏輯
#             if i > order_i + 3 and c_close > c_open:
#                position = 0
#                cover_time=n_time
#                cover_price=n_open

#                trade=trade.append(
                   
#                    pd.Series(
#                        [prod,'Buy',order_time,order_price,
#                         cover_time,cover_price]),ignore_index=True
#                )
#                print(trade)





