import twstock as t
import pandas as pd
import plotly.express as e



pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.width',80)
pd.set_option("display.max_columns",1000000000)

stock=t.Stock('6188')
date=stock.date
price=stock.price
amount=stock.capacity

data=pd.DataFrame({'日期':date,'廣明收盤價':price})
result=e.line(data, x='日期',y='廣明收盤價',title='收盤價即時資料')
result.show()

data=pd.DataFrame({'日期':date,'成交量':amount})
result=e.bar(data, x='日期',y='成交量',title='成交量即時資料')
result.show()



# stock=t.realtime.get('1101')
# print(stock['success'])
# result=pd.DataFrame(stock).T.iloc[1:3]
# result.columns=['股票代碼','地區','股票名稱','公司全名','現在時間','最新成交價','成交量','累積成交量','最佳五檔賣出價','最佳五檔賣出量','最佳五檔買進價','最佳五檔買進量','開盤價','最高價','最低價']
# print(result)