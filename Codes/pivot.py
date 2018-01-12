import pandas as  pd
import csv
from itertools import izip
a = izip(*csv.reader(open("/home/sidhant/pro_new/pen_2/final_2/final_frames.csv", "rb")))
csv.writer(open("pivot_asia.csv", "wb")).writerows(a)
df = pd.read_csv('pivot_asia.csv')
df1 = pd.DataFrame(df)
df1.to_excel('asia_pivot.xlsx')