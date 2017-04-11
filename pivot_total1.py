import pandas as  pd
import csv
from itertools import izip
a = izip(*csv.reader(open("/home/sidhant/pro_new/pen_2/final_2/40/final_frames.csv", "rb")))
csv.writer(open("pivot_total.csv", "wb")).writerows(a)
df = pd.read_csv('pivot_total.csv')
df1 = pd.DataFrame(df)
normalize=['East Asia','South Asia','Southeast Asia','Western Asia','Caucacus and Central Asia']
df1[normalize]=df1[normalize].apply(lambda x: (x / 1000))
df1.to_excel('pivot_total.xlsx')