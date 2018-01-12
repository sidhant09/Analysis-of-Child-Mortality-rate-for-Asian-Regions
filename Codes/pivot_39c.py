import pandas as  pd
import csv
from itertools import izip
a = izip(*csv.reader(open("/home/sidhant/pro_new/pen_2/final_2/final_frames_39c.csv", "rb")))
csv.writer(open("pivot_39c.csv", "wb")).writerows(a)
df = pd.read_csv('pivot_39c.csv')
df1 = pd.DataFrame(df)
df1.to_excel('pivot_39c.xlsx')