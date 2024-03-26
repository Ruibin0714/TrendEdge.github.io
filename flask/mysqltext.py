import pandas as pd
import numpy as np
import urllib.request as request
import json
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width',180)

src='https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire&limit=100'
with request.urlopen(src) as response:
    data=json.load(response)

clist=data['result']['results']
print(clist)
with open('data.txt',mode='w',encoding='utf-8') as file:
    for company in clist:
        file.write(company['公司名稱'] + company['統編']+company['公司地址']+'\n')
    

# #定義類別
# class IO:
#     supportedSrcs=['console','file']
#     def read(src):
#         if src not in IO.supportedSrcs:
#             print('Not Supported')
#         else:
#             print('Read from',src)

#         print('Read from',src)
    


# print(IO.supportedSrcs)
# IO.read('file')
# IO.read('internet')   
