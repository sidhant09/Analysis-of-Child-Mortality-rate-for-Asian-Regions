import pandas as pd
import numpy as np

def abc():
	df = pd.read_excel('39a.xlsx')
	df1 = pd.DataFrame(df)
	df1.to_csv('39_data.csv')
	csv_file = pd.read_csv('39_data.csv')
	selected_columns_39a=csv_file[['ISO Code','Region Name','Uncertainity bounds','1990.5','1995.5','2000.5','2005.5','2010.5','2015.5']]
	thirty_nine_a=pd.DataFrame(selected_columns_39a)
	china_df=pd.read_csv('39_data.csv')
	china=['China']
	china_df=thirty_nine_a.loc[thirty_nine_a['Region Name'].isin(china)]
	china_df.to_csv('39_china_data.csv')
	china_df.reset_index(drop=True)
abc()
