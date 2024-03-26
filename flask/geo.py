import yfinance as yf
import pandas as pd
import numpy as np
from FinMind.data import DataLoader
import mplfinance as mpf
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width',180)

FM=DataLoader()
def getDataFM(prod,st,en):
    tmpData=FM.taiwan_stock_daily_adj(stock_id=prod,start_date=st,end_date=en)
    tmpData=tmpData.rename(columns={'max':'high','min':'low','Trading_Volume':'Volume'})
    tmpData['date']=pd.to_datetime(tmpData['date'])
    tmpData=tmpData.set_index(tmpData['date'])
    tmpData=tmpData[['open','high','low','close','Volume']]
    return tmpData


def ChartCandle(data,addp=[]):
    mcolor=mpf.make_marketcolors(up='r',down='g',inherit=True)
    mstyle=mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mcolor)
    mpf.plot(data,addplot=addp,style=mstyle,type='candle')



data=getDataFM('1609','2023-07-01','2023-07-31')
pd.DataFrame(data)
print(data)
ChartCandle(data)





# data=getDataFM('1609','2023-01-01','2023-07-21')
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
#     if position == 0:
#         #進場邏輯
#         if c_close>c_open and (c_close-c_open)*2<(c_open-c_low):
#             position = 1
#             order_i=i
#             order_time=n_time
#             order_price=n_open
#             order_unit=1

#         elif position ==1:
#             if i>order_i+3 and c_close > c_open:
#                 position=0
#                 cover_time=n_time
#                 cover_price=n_open

# trade=trade.append(pd.Series([prod,'BUY',order_time,order_price,cover_time,cover_price]),ignore_index=True)
# print(trade)                           


        



# # print(c_time,'觸發出場訊號,隔日出場',order_time,'出場價',order_price)



















# print(data)
# mpf.plot(data,type='candle',style=mstyle,title='3013')






# a=FM.taiwan_stock_daily_adj(stock_id='2317',start_date='2023-01-01',end_date='2023-07-23')
# print(a.iloc[:,[4,5,6,7]].mean())










# a=yf.download('3013.tw',period='7d',interval='2m')
# a=pd.DataFrame(a)


# def getDataYF(prod,st,en):
#     temData=yf.download(prod,start=st,end=en)
#     temData.columns=[i.lower() for i in temData.columns]
#     return temData













# req = request.get("https://fubon-ebrokerdj.fbs.com.tw/z/zg/zg_A_0_5.djhtm")
# html = req.text
# soup = BeautifulSoup(html)

# product =[i.text.strip() for i in soup.find_all("td", class_="t3t1")]
# print(product)


# result=pd.read_csv("weekly.csv")
# result.sort_values(['發病週別','年齡層'],ascending=[False,True])

# yy=result['縣市'].isin(['台北市','台中市','高雄市'])

# print(result[yy])
# print(result.columns)
