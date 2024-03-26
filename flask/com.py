import pandas as pd
import numpy as np

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width',180)
pd.set_option('display.max_column',None)


def convert_to_number(value):
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return value
    return value




a=pd.read_excel('客戶資料.xlsx',sheet_name='客戶資料彙總')

print(a.info())
print(a.shape)
print(a.describe(include=[np.object_]).T)
print(a.apply())  
# a['電話號碼'].str.replace("-","")
# a['電話號碼'].str.replace("#","").str.replace(".","").str.replace("EX","").str.replace("轉","")

# print(a)

# print(a['電話號碼'].isna().sum())


# a['電話號碼']=a['電話號碼'].apply(convert_to_number)

# print(a)
# a['new Length']=a['電話號碼'].str.len()
# print(a)

