import pandas as pd
import numpy as np

def abcic():
	df = pd.read_excel('/home/sidhant/pro_new/pen_2/final_2/39a.xlsx')
	df1 = pd.DataFrame(df)
	df1.to_csv('39a.csv')
	csv_file = pd.read_csv('39a.csv')
	selected_columns_39a=csv_file[['ISO Code','Region Name','Uncertainity bounds','1990.5','1995.5','2000.5','2005.5','2010.5','2015.5']]
	thirty_nine_a=pd.DataFrame(selected_columns_39a)
	#def india():	
	india=['India']
	india_df=thirty_nine_a.loc[thirty_nine_a['Region Name'].isin(india)]
	india_df.to_csv('39_india_data.csv')
	india_df.reset_index(drop=True)
	thirty_nine_india=pd.read_csv('39_india_data.csv')
	#
	thirty_nine_india_1990=india_df['1990.5']
	thirty_nine_india_1990=thirty_nine_india_1990.mean()
	thirty_nine_india_1990
	mean1_1990={'India':thirty_nine_india_1990}
	d1_1990=pd.Series(mean1_1990)
	d1_1990=pd.DataFrame(d1_1990)
	d1_1990.columns=['1990.5']
	d1_1990
	#
	thirty_nine_india_1995=india_df['1995.5']
	thirty_nine_india_1995=thirty_nine_india_1995.mean()
	thirty_nine_india_1995
	mean1_1995={'India':thirty_nine_india_1995}
	d1_1995=pd.Series(mean1_1995)
	d1_1995=pd.DataFrame(d1_1995)
	d1_1995.columns=['1995.5']
	d1_1995
	#
	thirty_nine_india_2000=india_df['2000.5']
	thirty_nine_india_2000=thirty_nine_india_2000.mean()
	thirty_nine_india_2000
	mean1_2000={'India':thirty_nine_india_2000}
	d1_2000=pd.Series(mean1_2000)
	d1_2000=pd.DataFrame(d1_2000)
	d1_2000.columns=['2000.5']
	d1_2000
	#
	thirty_nine_india_2005=india_df['2005.5']
	thirty_nine_india_2005=thirty_nine_india_2005.mean()
	thirty_nine_india_2005
	mean1_2005={'India':thirty_nine_india_2005}
	d1_2005=pd.Series(mean1_2005)
	d1_2005=pd.DataFrame(d1_2005)
	d1_2005.columns=['2005.5']
	d1_2005
	#	
	thirty_nine_india_2010=india_df['2010.5']
	thirty_nine_india_2010=thirty_nine_india_2010.mean()
	thirty_nine_india_2010
	mean1_2010={'India':thirty_nine_india_2010}
	d1_2010=pd.Series(mean1_2010)
	d1_2010=pd.DataFrame(d1_2010)
	d1_2010.columns=['2010.5']
	d1_2010
	#
	thirty_nine_india_2015=india_df['2015.5']
	thirty_nine_india_2015=thirty_nine_india_2015.mean()
	thirty_nine_india_2015
	mean1_2015={'India':thirty_nine_india_2015}
	d1_2015=pd.Series(mean1_2015)
	d1_2015=pd.DataFrame(d1_2015)
	d1_2015.columns=['2015.5']
	d1_2015
	#
	india_1=pd.concat([d1_1990,d1_1995,d1_2000,d1_2005,d1_2010,d1_2015],axis=1,join_axes=[d1_1990.index])
	india_1
	india_1.to_csv('india_line.csv')
	#
	#def china():
	china=['China']
	china_df=thirty_nine_a.loc[thirty_nine_a['Region Name'].isin(china)]
	china_df.to_csv('39_china_data.csv')
	china_df.reset_index(drop=True)
	#
	thirty_nine_china_1990=china_df['1990.5']
	thirty_nine_china_1990=thirty_nine_china_1990.mean()
	thirty_nine_china_1990
	mean4_1990={'China':thirty_nine_china_1990}
	d4_1990=pd.Series(mean4_1990)
	d4_1990=pd.DataFrame(d4_1990)
	d4_1990.columns=['1990.5']
	d4_1990
	#
	thirty_nine_china_1995=china_df['1995.5']
	thirty_nine_china_1995=thirty_nine_china_1995.mean()
	thirty_nine_china_1995
	mean4_1995={'China':thirty_nine_china_1995}
	d4_1995=pd.Series(mean4_1995)
	d4_1995=pd.DataFrame(d4_1995)
	d4_1995.columns=['1995.5']
	d4_1995
	#
	thirty_nine_china_2005=china_df['2005.5']
	thirty_nine_china_2005=thirty_nine_china_2005.mean()
	thirty_nine_china_2005
	mean4_2005={'China':thirty_nine_china_2005}
	d4_2005=pd.Series(mean4_2005)
	d4_2005=pd.DataFrame(d4_2005)
	d4_2005.columns=['2005.5']
	d4_2005
	#
	thirty_nine_china_2000=china_df['2000.5']
	thirty_nine_china_2000=thirty_nine_china_2000.mean()
	thirty_nine_china_2000
	mean4_2000={'China':thirty_nine_china_2000}
	d4_2000=pd.Series(mean4_2000)
	d4_2000=pd.DataFrame(d4_2000)
	d4_2000.columns=['2000.5']
	d4_2000
	#
	thirty_nine_china_2010=china_df['2010.5']
	thirty_nine_china_2010=thirty_nine_china_2010.mean()
	thirty_nine_china_2010
	mean4_2010={'China':thirty_nine_china_2010}
	d4_2010=pd.Series(mean4_2010)
	d4_2010=pd.DataFrame(d4_2010)
	d4_2010.columns=['2010.5']
	d4_2010
	#
	#
	thirty_nine_china_2015=china_df['2015.5']
	thirty_nine_china_2015=thirty_nine_china_2015.mean()
	thirty_nine_china_2015
	mean4_2015={'China':thirty_nine_china_2015}
	d4_2015=pd.Series(mean4_2015)
	d4_2015=pd.DataFrame(d4_2015)
	d4_2015.columns=['2015.5']
	d4_2015
	#
	china_1=pd.concat([d4_1990,d4_1995,d4_2000,d4_2005,d4_2010,d4_2015],axis=1,join_axes=[d4_1990.index])
	china_1
	china_1.to_csv('china_line.csv')
	#
	#
	frames_1 = [india_1,china_1]
	final_frames_1 = pd.concat(frames_1)
	final_frames_1.to_csv('final_frames_1.csv')
	final_frames_1
abcic()