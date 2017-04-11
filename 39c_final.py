import pandas as pd
import numpy as np

def abc():
	df = pd.read_excel('/home/sidhant/pro_new/pen_2/final_2/39c.xlsx')
	df1 = pd.DataFrame(df)
	df1.to_csv('39c.csv')
	csv_file = pd.read_csv('39c.csv')
	selected_columns_39c=csv_file[['Region Name','Uncertainity bounds','1990.5','1995.5','2000.5','2005.5','2010.5','2015.5']]
	forty_a=pd.DataFrame(selected_columns_39c)
	#def eastasia():	
	central_asia=['Caucasus and Central Asia']
	central_asia_df=forty_a.loc[forty_a['Region Name'].isin(central_asia)]
	central_asia_df.to_csv('39_centralasia_data.csv')
	central_asia_df.reset_index(drop=True)
	forty_centralasia=pd.read_csv('39_centralasia_data.csv')
	#
	forty_centralasia_1990=central_asia_df['1990.5']
	forty_centralasia_1990=forty_centralasia_1990.mean()
	forty_centralasia_1990
	mean1_1990={'Caucasus and Central Asia':forty_centralasia_1990}
	d1_1990=pd.Series(mean1_1990)
	d1_1990=pd.DataFrame(d1_1990)
	d1_1990.columns=['1990.5']
	d1_1990
	#
	forty_centralasia_1995=central_asia_df['1995.5']
	forty_centralasia_1995=forty_centralasia_1995.mean()
	forty_centralasia_1995
	mean1_1995={'Caucasus and Central Asia':forty_centralasia_1995}
	d1_1995=pd.Series(mean1_1995)
	d1_1995=pd.DataFrame(d1_1995)
	d1_1995.columns=['1995.5']
	d1_1995
	#
	forty_centralasia_2000=central_asia_df['2000.5']
	forty_centralasia_2000=forty_centralasia_2000.mean()
	forty_centralasia_2000
	mean1_2000={'Caucasus and Central Asia':forty_centralasia_2000}
	d1_2000=pd.Series(mean1_2000)
	d1_2000=pd.DataFrame(d1_2000)
	d1_2000.columns=['2000.5']
	d1_2000
	#
	forty_centralasia_2005=central_asia_df['2005.5']
	forty_centralasia_2005=forty_centralasia_2005.mean()
	forty_centralasia_2005
	mean1_2005={'Caucasus and Central Asia':forty_centralasia_2005}
	d1_2005=pd.Series(mean1_2005)
	d1_2005=pd.DataFrame(d1_2005)
	d1_2005.columns=['2005.5']
	d1_2005
	#
	forty_centralasia_2010=central_asia_df['2010.5']
	forty_centralasia_2010=forty_centralasia_2010.mean()
	forty_centralasia_2010
	mean1_2010={'Caucasus and Central Asia':forty_centralasia_2010}
	d1_2010=pd.Series(mean1_2010)
	d1_2010=pd.DataFrame(d1_2010)
	d1_2010.columns=['2010.5']
	d1_2010
	#
	forty_centralasia_2015=central_asia_df['2015.5']
	forty_centralasia_2015=forty_centralasia_2015.mean()
	forty_centralasia_2015
	mean1_2015={'Caucasus and Central Asia':forty_centralasia_2015}
	d1_2015=pd.Series(mean1_2015)
	d1_2015=pd.DataFrame(d1_2015)
	d1_2015.columns=['2015.5']
	d1_2015
	#
	central_asia_1=pd.concat([d1_1990,d1_1995,d1_2000,d1_2005,d1_2010,d1_2015],axis=1,join_axes=[d1_1990.index])
	central_asia_1
	central_asia_1.to_csv('central_asia_1.csv')
	#def easternasia():
	eastern_asia=['Eastern Asia']
	eastern_asia_df=forty_a.loc[forty_a['Region Name'].isin(eastern_asia)]
	eastern_asia_df.to_csv('39_easternasia_data.csv')
	eastern_asia_df.reset_index(drop=True)
	forty_easternasia=pd.read_csv('39_easternasia_data.csv')
	#
	forty_easternasia_1990=eastern_asia_df['1990.5']
	forty_easternasia_1990=forty_easternasia_1990.mean()
	forty_easternasia_1990
	mean2_1990={'Eastern Asia':forty_easternasia_1990}
	d2_1990=pd.Series(mean2_1990)
	d2_1990=pd.DataFrame(d2_1990)
	d2_1990.columns=['1990.5']
	d2_1990
	#
	forty_easternasia_1995=eastern_asia_df['1995.5']
	forty_easternasia_1995=forty_easternasia_1995.mean()
	forty_easternasia_1995
	mean2_1995={'Eastern Asia':forty_easternasia_1995}
	d2_1995=pd.Series(mean2_1995)
	d2_1995=pd.DataFrame(d2_1995)
	d2_1995.columns=['1995.5']
	d2_1995
	#
	forty_easternasia_2000=eastern_asia_df['2000.5']
	forty_easternasia_2000=forty_easternasia_2000.mean()
	forty_easternasia_2000
	mean2_2000={'Eastern Asia':forty_easternasia_2000}
	d2_2000=pd.Series(mean2_2000)
	d2_2000=pd.DataFrame(d2_2000)
	d2_2000.columns=['2000.5']
	d2_2000
	#
	forty_easternasia_2005=eastern_asia_df['2005.5']
	forty_easternasia_2005=forty_easternasia_2005.mean()
	forty_easternasia_2005
	mean2_2005={'Eastern Asia':forty_easternasia_2005}
	d2_2005=pd.Series(mean2_2005)
	d2_2005=pd.DataFrame(d2_2005)
	d2_2005.columns=['2005.5']
	d2_2005
	#
	forty_easternasia_2010=eastern_asia_df['2010.5']
	forty_easternasia_2010=forty_easternasia_2010.mean()
	forty_easternasia_2010
	mean2_2010={'Eastern Asia':forty_easternasia_2010}
	d2_2010=pd.Series(mean2_2010)
	d2_2010=pd.DataFrame(d2_2010)
	d2_2010.columns=['2010.5']
	d2_2010
	#
	forty_easternasia_2015=eastern_asia_df['2015.5']
	forty_easternasia_2015=forty_easternasia_2015.mean()
	forty_easternasia_2015
	mean2_2015={'Eastern Asia':forty_easternasia_2015}
	d2_2015=pd.Series(mean2_2015)
	d2_2015=pd.DataFrame(d2_2015)
	d2_2015.columns=['2015.5']
	d2_2015
	#
	eastern_asia_1=pd.concat([d2_1990,d2_1995,d2_2000,d2_2005,d2_2010,d2_2015],axis=1,join_axes=[d2_1990.index])
	eastern_asia_1
	eastern_asia_1.to_csv('eastern_asia_1.csv')
	#def eastexchina():
	eastexchina=['Eastern Asia excluding China']
	eastexchina_df=forty_a.loc[forty_a['Region Name'].isin(eastexchina)]
	eastexchina_df.to_csv('39_eastexchina_data.csv')
	eastexchina_df.reset_index(drop=True)
	forty_eastexchina=pd.read_csv('39_eastexchina_data.csv')
	#
	forty_eastexchina_1990=eastexchina_df['1990.5']
	forty_eastexchina_1990=forty_eastexchina_1990.mean()
	forty_eastexchina_1990
	mean3_1990={'Eastern Asia excluding China':forty_eastexchina_1990}
	d3_1990=pd.Series(mean3_1990)
	d3_1990=pd.DataFrame(d3_1990)
	d3_1990.columns=['1990.5']
	d3_1990
	#
	forty_eastexchina_1995=eastexchina_df['1995.5']
	forty_eastexchina_1995=forty_eastexchina_1995.mean()
	forty_eastexchina_1995
	mean3_1995={'Eastern Asia excluding China':forty_eastexchina_1995}
	d3_1995=pd.Series(mean3_1995)
	d3_1995=pd.DataFrame(d3_1995)
	d3_1995.columns=['1995.5']
	d3_1995
	#
	forty_eastexchina_2000=eastexchina_df['2000.5']
	forty_eastexchina_2000=forty_eastexchina_2000.mean()
	forty_eastexchina_2000
	mean3_2000={'Eastern Asia excluding China':forty_eastexchina_2000}
	d3_2000=pd.Series(mean3_2000)
	d3_2000=pd.DataFrame(d3_2000)
	d3_2000.columns=['2000.5']
	d3_2000
	#
	forty_eastexchina_2005=eastexchina_df['2005.5']
	forty_eastexchina_2005=forty_eastexchina_2005.mean()
	forty_eastexchina_2005
	mean3_2005={'Eastern Asia excluding China':forty_eastexchina_2005}
	d3_2005=pd.Series(mean3_2005)
	d3_2005=pd.DataFrame(d3_2005)
	d3_2005.columns=['2005.5']
	d3_2005
	#
	forty_eastexchina_2010=eastexchina_df['2010.5']
	forty_eastexchina_2010=forty_eastexchina_2010.mean()
	forty_eastexchina_2010
	mean3_2010={'Eastern Asia excluding China':forty_eastexchina_2010}
	d3_2010=pd.Series(mean3_2010)
	d3_2010=pd.DataFrame(d3_2010)
	d3_2010.columns=['2010.5']
	d3_2010
	#
	forty_eastexchina_2015=eastexchina_df['2015.5']
	forty_eastexchina_2015=forty_eastexchina_2015.mean()
	forty_eastexchina_2015
	mean3_2015={'Eastern Asia excluding China':forty_eastexchina_2015}
	d3_2015=pd.Series(mean3_2015)
	d3_2015=pd.DataFrame(d3_2015)
	d3_2015.columns=['2015.5']
	d3_2015
	#
	eastexchina_1=pd.concat([d3_1990,d3_1995,d3_2000,d3_2005,d3_2010,d3_2015],axis=1,join_axes=[d3_1990.index])
	eastexchina_1
	eastexchina_1.to_csv('eastexchina_1.csv')
	
	#
	#def southernasiaexindia():
	southexindia=['Southern Asia excluding India']
	southexindia_df=forty_a.loc[forty_a['Region Name'].isin(southexindia)]
	southexindia_df.to_csv('39_southexindia_data.csv')
	southexindia_df.reset_index(drop=True)
	forty_southexindia=pd.read_csv('39_southexindia_data.csv')
	#
	forty_southexindia_1990=southexindia_df['1990.5']
	forty_southexindia_1990=forty_southexindia_1990.mean()
	forty_southexindia_1990
	mean4_1990={'Southern Asia excluding India':forty_southexindia_1990}
	d4_1990=pd.Series(mean4_1990)
	d4_1990=pd.DataFrame(d4_1990)
	d4_1990.columns=['1990.5']
	d4_1990
	#
	forty_southexindia_1995=southexindia_df['1995.5']
	forty_southexindia_1995=forty_southexindia_1995.mean()
	forty_southexindia_1995
	mean4_1995={'Southern Asia excluding India':forty_southexindia_1995}
	d4_1995=pd.Series(mean4_1995)
	d4_1995=pd.DataFrame(d4_1995)
	d4_1995.columns=['1995.5']
	d4_1995
	#
	forty_southexindia_2000=southexindia_df['2000.5']
	forty_southexindia_2000=forty_southexindia_2000.mean()
	forty_southexindia_2000
	mean4_2000={'Southern Asia excluding India':forty_southexindia_2000}
	d4_2000=pd.Series(mean4_2000)
	d4_2000=pd.DataFrame(d4_2000)
	d4_2000.columns=['2000.5']
	d4_2000
	#
	forty_southexindia_2005=southexindia_df['2005.5']
	forty_southexindia_2005=forty_southexindia_2005.mean()
	forty_southexindia_2005
	mean4_2005={'Southern Asia excluding India':forty_southexindia_2005}
	d4_2005=pd.Series(mean4_2005)
	d4_2005=pd.DataFrame(d4_2005)
	d4_2005.columns=['2005.5']
	d4_2005
	#
	forty_southexindia_2010=southexindia_df['2010.5']
	forty_southexindia_2010=forty_southexindia_2010.mean()
	forty_southexindia_2010
	mean4_2010={'Southern Asia excluding India':forty_southexindia_2010}
	d4_2010=pd.Series(mean4_2010)
	d4_2010=pd.DataFrame(d4_2010)
	d4_2010.columns=['2010.5']
	d4_2010
	#
	forty_southexindia_2015=southexindia_df['2015.5']
	forty_southexindia_2015=forty_southexindia_2015.mean()
	forty_southexindia_2015
	mean4_2015={'Southern Asia excluding India':forty_southexindia_2015}
	d4_2015=pd.Series(mean4_2015)
	d4_2015=pd.DataFrame(d4_2015)
	d4_2015.columns=['2015.5']
	d4_2015
	#
	southexindia_1=pd.concat([d4_1990,d4_1995,d4_2000,d4_2005,d4_2010,d4_2015],axis=1,join_axes=[d4_1990.index])
	southexindia_1
	southexindia_1.to_csv('southexindia_1.csv')
	#def sotheastasia()
	southern_asia=['Southern Asia']
	southern_asia_df=forty_a.loc[forty_a['Region Name'].isin(southern_asia)]
	southern_asia_df.to_csv('39_south_data.csv')
	southern_asia_df.reset_index(drop=True)
	forty_southern_asia=pd.read_csv('39_south_data.csv')

	#
	forty_southern_asia_1990=southern_asia_df['1990.5']
	forty_southern_asia_1990=forty_southern_asia_1990.mean()
	forty_southern_asia_1990
	mean5_1990={'Southern Eastern Asia':forty_southern_asia_1990}
	d5_1990=pd.Series(mean5_1990)
	d5_1990=pd.DataFrame(d5_1990)
	d5_1990.columns=['1990.5']
	d5_1990
	#
	forty_southern_asia_1995=southern_asia_df['1995.5']
	forty_southern_asia_1995=forty_southern_asia_1995.mean()
	forty_southern_asia_1995
	mean5_1995={'Southern Eastern Asia':forty_southern_asia_1995}
	d5_1995=pd.Series(mean5_1995)
	d5_1995=pd.DataFrame(d5_1995)
	d5_1995.columns=['1995.5']
	d5_1995
	#
	forty_southern_asia_2000=southern_asia_df['2000.5']
	forty_southern_asia_2000=forty_southern_asia_2000.mean()
	forty_southern_asia_2000
	mean5_2000={'Southern Eastern Asia':forty_southern_asia_2000}
	d5_2000=pd.Series(mean5_2000)
	d5_2000=pd.DataFrame(d5_2000)
	d5_2000.columns=['2000.5']
	d5_2000	
	#
	forty_southern_asia_2005=southern_asia_df['2005.5']
	forty_southern_asia_2005=forty_southern_asia_2005.mean()
	forty_southern_asia_2005
	mean5_2005={'Southern Eastern Asia':forty_southern_asia_2005}
	d5_2005=pd.Series(mean5_2005)
	d5_2005=pd.DataFrame(d5_2005)
	d5_2005.columns=['2005.5']
	d5_2005
	#
	forty_southern_asia_2010=southern_asia_df['2010.5']
	forty_southern_asia_2010=forty_southern_asia_2010.mean()
	forty_southern_asia_2010
	mean5_2010={'Southern Eastern Asia':forty_southern_asia_2010}
	d5_2010=pd.Series(mean5_2010)
	d5_2010=pd.DataFrame(d5_2010)
	d5_2010.columns=['2010.5']
	d5_2010
	#
	forty_southern_asia_2015=southern_asia_df['2015.5']
	forty_southern_asia_2015=forty_southern_asia_2015.mean()
	forty_southern_asia_2015
	mean5_2015={'Southern Eastern Asia':forty_southern_asia_2015}
	d5_2015=pd.Series(mean5_2015)
	d5_2015=pd.DataFrame(d5_2015)
	d5_2015.columns=['2015.5']
	d5_2015
	southern_asia_1=pd.concat([d5_1990,d5_1995,d5_2000,d5_2005,d5_2010,d5_2015],axis=1,join_axes=[d5_1990.index])
	southern_asia_1
	southern_asia_1.to_csv('southern_asia_1.csv')
	#def westernasia()
	western_asia=['Western Asia']
	western_asia_df=forty_a.loc[forty_a['Region Name'].isin(western_asia)]
	western_asia_df.to_csv('39_western_data.csv')
	western_asia_df.reset_index(drop=True)
	forty_western_asia=pd.read_csv('39_western_data.csv')
	#
	forty_western_asia_1990=western_asia_df['1990.5']
	forty_western_asia_1990=forty_western_asia_1990.mean()
	forty_western_asia_1990
	mean6_1990={'Western Asia':forty_western_asia_1990}
	d6_1990=pd.Series(mean6_1990)
	d6_1990=pd.DataFrame(d6_1990)
	d6_1990.columns=['1990.5']
	d6_1990
	#
	forty_western_asia_1995=western_asia_df['1995.5']
	forty_western_asia_1995=forty_western_asia_1995.mean()
	forty_western_asia_1995
	mean6_1995={'Western Asia':forty_western_asia_1995}
	d6_1995=pd.Series(mean6_1995)
	d6_1995=pd.DataFrame(d6_1995)
	d6_1995.columns=['1995.5']
	d6_1995
	#
	forty_western_asia_2000=western_asia_df['2000.5']
	forty_western_asia_2000=forty_western_asia_2000.mean()
	forty_western_asia_2000
	mean6_2000={'Western Asia':forty_western_asia_2000}
	d6_2000=pd.Series(mean6_2000)
	d6_2000=pd.DataFrame(d6_2000)
	d6_2000.columns=['2000.5']
	d6_2000
	#
	forty_western_asia_2005=western_asia_df['2005.5']
	forty_western_asia_2005=forty_western_asia_2005.mean()
	forty_western_asia_2005
	mean6_2005={'Western Asia':forty_western_asia_2005}
	d6_2005=pd.Series(mean6_2005)
	d6_2005=pd.DataFrame(d6_2005)
	d6_2005.columns=['2005.5']
	d6_2005
	#
	forty_western_asia_2010=western_asia_df['2010.5']
	forty_western_asia_2010=forty_western_asia_2010.mean()
	forty_western_asia_2010
	mean6_2010={'Western Asia':forty_western_asia_2010}
	d6_2010=pd.Series(mean6_2010)
	d6_2010=pd.DataFrame(d6_2010)
	d6_2010.columns=['2010.5']
	d6_2010
	#
	forty_western_asia_2015=western_asia_df['2015.5']
	forty_western_asia_2015=forty_western_asia_2015.mean()
	forty_western_asia_2015
	mean6_2015={'Western Asia':forty_western_asia_2015}
	d6_2015=pd.Series(mean6_2015)
	d6_2015=pd.DataFrame(d6_2015)
	d6_2015.columns=['2015.5']
	d6_2015
	#
	western_asia_1=pd.concat([d6_1990,d6_1995,d6_2000,d6_2005,d6_2010,d6_2015],axis=1,join_axes=[d6_1990.index])
	western_asia_1
	western_asia_1.to_csv('western_asia_1.csv')
	#
	south_east_asia=['South-eastern Asia']
	south_east_asia_df=forty_a.loc[forty_a['Region Name'].isin(south_east_asia)]
	south_east_asia_df.to_csv('39_southeastasia_data.csv')
	south_east_asia_df.reset_index(drop=True)
	forty_south_east_asia=pd.read_csv('39_southeastasia_data.csv')
	#
	forty_southernasia_1990=south_east_asia_df['1990.5']
	forty_southernasia_1990=forty_southernasia_1990.mean()
	forty_southernasia_1990
	mean4_1990={'Southern Asia':forty_southernasia_1990}
	d7_1990=pd.Series(mean4_1990)
	d7_1990=pd.DataFrame(d7_1990)
	d7_1990.columns=['1990.5']
	d7_1990
	#
	forty_southernasia_1995=south_east_asia_df['1995.5']
	forty_southernasia_1995=forty_southernasia_1995.mean()
	forty_southernasia_1995
	mean4_1995={'Southern Asia':forty_southernasia_1995}
	d7_1995=pd.Series(mean4_1995)
	d7_1995=pd.DataFrame(d7_1995)
	d7_1995.columns=['1995.5']
	d7_1995
	#
	forty_southernasia_2000=south_east_asia_df['2000.5']
	forty_southernasia_2000=forty_southernasia_2000.mean()
	forty_southernasia_2000
	mean4_2000={'Southern Asia':forty_southernasia_2000}
	d7_2000=pd.Series(mean4_2000)
	d7_2000=pd.DataFrame(d7_2000)
	d7_2000.columns=['2000.5']
	d7_2000
	#
	forty_southernasia_2005=south_east_asia_df['2005.5']
	forty_southernasia_2005=forty_southernasia_2005.mean()
	forty_southernasia_2005
	mean4_2005={'Southern Asia':forty_southernasia_2005}
	d7_2005=pd.Series(mean4_2005)
	d7_2005=pd.DataFrame(d7_2005)
	d7_2005.columns=['2005.5']
	d7_2005
	#
	forty_southernasia_2010=south_east_asia_df['2010.5']
	forty_southernasia_2010=forty_southernasia_2010.mean()
	forty_southernasia_2010
	mean4_2010={'Southern Asia':forty_southernasia_2010}
	d7_2010=pd.Series(mean4_2010)
	d7_2010=pd.DataFrame(d7_2010)
	d7_2010.columns=['2010.5']
	d7_2010
	#
	forty_southernasia_2015=south_east_asia_df['2015.5']
	forty_southernasia_2015=forty_southernasia_2015.mean()
	forty_southernasia_2015
	mean4_2015={'Southern Asia':forty_southernasia_2015}
	d7_2015=pd.Series(mean4_2015)
	d7_2015=pd.DataFrame(d7_2015)
	d7_2015.columns=['2015.5']
	d7_2015
	#
	south_east_asia_1=pd.concat([d7_1990,d7_1995,d7_2000,d7_2005,d7_2010,d7_2015],axis=1,join_axes=[d7_1990.index])
	south_east_asia_1
	south_east_asia_1.to_csv('south_east_asia_1.csv')
	#
	frames_1 = [central_asia_1,eastern_asia_1,eastexchina_1,southexindia_1,southern_asia_1,western_asia_1,south_east_asia_1]
	final_frames1 = pd.concat(frames_1)
	final_frames1.to_csv('final_frames_39c.csv')
	final_frames1
abc()
