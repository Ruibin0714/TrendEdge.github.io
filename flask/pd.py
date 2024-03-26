import numpy as np
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.width',80)

# movie=pd.read_csv('movie.csv')
# print(movie.iloc[:,1].name)
# s_arr=set(dir(pd.Series))
# print(len(s_arr))
# y_arr=set(dir(pd.DataFrame))
# print(len(y_arr))
# print(len(s_arr&y_arr))


number=1
sum=0
while number<100:
   sum+=number
   number+=1 
print(sum)








