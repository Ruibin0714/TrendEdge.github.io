import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.width',80)


# movie=pd.read_csv('movie.csv')
# def shorten(col):
#     return(col.replace('facebook_likes','fb')
#                 .replace('_for_reviews',''))
# movie=movie.rename(columns=shorten)
# print(movie.isna().sum().sum())
# print(movie.isna().any())
colleges=pd.read_csv('college.csv',index_col='INSTNM')
print(colleges)
college_ugds=colleges.filter(like='UGDS_')
print(college_ugds.head())
name='University of Alabama in Huntsville'
print(college_ugds.loc[name].round(2))
print((college_ugds.loc[name]+0.01).round(2))
print((college_ugds+.001).round(2))

