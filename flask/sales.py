import pandas as pd
import numpy as np

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width',180)
pd.set_option('display.max_column',None)
sales=pd.read_excel('台中銷貨分析.xlsx',skiprows=14,index_col=0)
sales=sales.iloc[:,[0,1,2,5]]
sales.iloc[:,2].fillna(method='pad',inplace=True)
sale=sales[sales.iloc[:,1].notnull()]
se=sale[~sale.iloc[:,0].str.contains('產品大類')]
sy=se.sort_values(by='銷貨數量',ascending=False)

# s1=sy.iloc[:,3]>20
# s2=sy.iloc[:,0]=='CRS1.56單'



y=sy.groupby(['銷貨數量'])
print(y['客戶名稱'].value_counts().sort_values(ascending=False))

















































