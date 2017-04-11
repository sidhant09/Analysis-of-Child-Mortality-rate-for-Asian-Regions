import pandas as pd
import numpy as np

def abc():
	df = pd.read_excel('/home/sidhant/pro_new/pen_2/final_2/39a.xlsx')
	df1 = pd.DataFrame(df)
	df1.to_csv('39a.csv')
	csv_file = pd.read_csv('39a.csv')
	selected_columns_39a=csv_file[['ISO Code','Region Name','Uncertainity bounds','1990.5','1995.5','2000.5','2005.5','2010.5','2015.5']]
	thirty_nine_a=pd.DataFrame(selected_columns_39a)
	#def eastasia():	
	east_asia=['China','Japan','Republic of Korea','Mongolia',"Democratic People's Republic of Korea"]
	east_asia_df=thirty_nine_a.loc[thirty_nine_a['Region Name'].isin(east_asia)]
	east_asia_df.to_csv('39_eastasia_data.csv')
	east_asia_df.reset_index(drop=True)
	thirty_nine_eastasia=pd.read_csv('39_eastasia_data.csv')
	#
	thirty_nine_eastasia_1990=east_asia_df['1990.5']
	thirty_nine_eastasia_1990=thirty_nine_eastasia_1990.mean()
	thirty_nine_eastasia_1990
	mean1_1990={'East Asia':thirty_nine_eastasia_1990}
	d1_1990=pd.Series(mean1_1990)
	d1_1990=pd.DataFrame(d1_1990)
	d1_1990.columns=['1990.5']
	d1_1990
	#
	thirty_nine_eastasia_1995=east_asia_df['1995.5']
	thirty_nine_eastasia_1995=thirty_nine_eastasia_1995.mean()
	thirty_nine_eastasia_1995
	mean1_1995={'East Asia':thirty_nine_eastasia_1995}
	d1_1995=pd.Series(mean1_1995)
	d1_1995=pd.DataFrame(d1_1995)
	d1_1995.columns=['1995.5']
	d1_1995
	#
	thirty_nine_eastasia_2000=east_asia_df['2000.5']
	thirty_nine_eastasia_2000=thirty_nine_eastasia_2000.mean()
	thirty_nine_eastasia_2000
	mean1_2000={'East Asia':thirty_nine_eastasia_2000}
	d1_2000=pd.Series(mean1_2000)
	d1_2000=pd.DataFrame(d1_2000)
	d1_2000.columns=['2000.5']
	d1_2000
	#
	thirty_nine_eastasia_2005=east_asia_df['2005.5']
	thirty_nine_eastasia_2005=thirty_nine_eastasia_2005.mean()
	thirty_nine_eastasia_2005
	mean1_2005={'East Asia':thirty_nine_eastasia_2005}
	d1_2005=pd.Series(mean1_2005)
	d1_2005=pd.DataFrame(d1_2005)
	d1_2005.columns=['2005.5']
	d1_2005
	#	
	thirty_nine_eastasia_2010=east_asia_df['2010.5']
	thirty_nine_eastasia_2010=thirty_nine_eastasia_2010.mean()
	thirty_nine_eastasia_2010
	mean1_2010={'East Asia':thirty_nine_eastasia_2010}
	d1_2010=pd.Series(mean1_2010)
	d1_2010=pd.DataFrame(d1_2010)
	d1_2010.columns=['2010.5']
	d1_2010
	#
	thirty_nine_eastasia_2015=east_asia_df['2015.5']
	thirty_nine_eastasia_2015=thirty_nine_eastasia_2015.mean()
	thirty_nine_eastasia_2015
	mean1_2015={'East Asia':thirty_nine_eastasia_2015}
	d1_2015=pd.Series(mean1_2015)
	d1_2015=pd.DataFrame(d1_2015)
	d1_2015.columns=['2015.5']
	d1_2015
	#
	east_asia_1=pd.concat([d1_1990,d1_1995,d1_2000,d1_2005,d1_2010,d1_2015],axis=1,join_axes=[d1_1990.index])
	east_asia_1
	east_asia_1.to_csv('east_asia_1.csv')
	#def southasia():
	south_asia=south_asia=['Afghanistan','Bangladesh','Bhutan','India','Sri Lanka','Maldives','Nepal','Pakistan']
	south_asia_df=thirty_nine_a.loc[thirty_nine_a['Region Name'].isin(south_asia)]
	south_asia_df.to_csv('39_southasia_data.csv')
	south_asia_df.reset_index(drop=True)
	thirty_nine_southasia=pd.read_csv('39_southasia_data.csv')
	#
	thirty_nine_southasia_1990=south_asia_df['1990.5']
	thirty_nine_southasia_1990=thirty_nine_southasia_1990.mean()
	thirty_nine_southasia_1990
	mean2_1990={'South Asia':thirty_nine_southasia_1990}
	d2_1990=pd.Series(mean2_1990)
	d2_1990=pd.DataFrame(d2_1990)
	d2_1990.columns=['1990.5']
	d2_1990
	#
	thirty_nine_southasia_1995=south_asia_df['1995.5']
	thirty_nine_southasia_1995=thirty_nine_southasia_1995.mean()
	thirty_nine_southasia_1995
	mean2_1995={'South Asia':thirty_nine_southasia_1995}
	d2_1995=pd.Series(mean2_1995)
	d2_1995=pd.DataFrame(d2_1995)
	d2_1995.columns=['1995.5']
	d2_1995
	#
	thirty_nine_southasia_2005=south_asia_df['2005.5']
	thirty_nine_southasia_2005=thirty_nine_southasia_2005.mean()
	thirty_nine_southasia_2005
	mean2_2005={'South Asia':thirty_nine_southasia_2005}
	d2_2005=pd.Series(mean2_2005)
	d2_2005=pd.DataFrame(d2_2005)
	d2_2005.columns=['2005.5']
	d2_2005
	#
	thirty_nine_southasia_2000=south_asia_df['2000.5']
	thirty_nine_southasia_2000=thirty_nine_southasia_2000.mean()
	thirty_nine_southasia_2000
	mean2_2000={'South Asia':thirty_nine_southasia_2000}
	d2_2000=pd.Series(mean2_2000)
	d2_2000=pd.DataFrame(d2_2000)
	d2_2000.columns=['2000.5']
	d2_2000
	#
	thirty_nine_southasia_2010=south_asia_df['2010.5']
	thirty_nine_southasia_2010=thirty_nine_southasia_2010.mean()
	thirty_nine_southasia_2010
	mean2_2010={'South Asia':thirty_nine_southasia_2010}
	d2_2010=pd.Series(mean2_2010)
	d2_2010=pd.DataFrame(d2_2010)
	d2_2010.columns=['2010.5']
	d2_2010
	#
	thirty_nine_southasia_2015=south_asia_df['2015.5']
	thirty_nine_southasia_2015=thirty_nine_southasia_2015.mean()
	thirty_nine_southasia_2015
	mean2_2015={'South Asia':thirty_nine_southasia_2015}
	d2_2015=pd.Series(mean2_2015)
	d2_2015=pd.DataFrame(d2_2015)
	d2_2015.columns=['2015.5']
	d2_2015
	#
	south_asia_1=pd.concat([d2_1990,d2_1995,d2_2000,d2_2005,d2_2010,d2_2015],axis=1,join_axes=[d2_1990.index])
	south_asia_1
	south_asia_1.to_csv('south_asia_1.csv')
	#def southeastasia():
	south_east_asia=['Brunei Darussalam','Indonesia','Cambodia','Myanmar','Malaysia','Philippines','Singapore','Thailand','Timor-Leste','Viet Nam']
	south_east_asia_df=thirty_nine_a.loc[thirty_nine_a['Region Name'].isin(south_east_asia)]
	south_east_asia_df.to_csv('39_southeastasia_data.csv')
	south_east_asia_df.reset_index(drop=True)
	#
	thirty_nine_southeastasia_1990=south_east_asia_df['1990.5']
	thirty_nine_southeastasia_1990=thirty_nine_southeastasia_1990.mean()
	thirty_nine_southeastasia_1990
	mean3_1990={'Southeast Asia':thirty_nine_southeastasia_1990}
	d3_1990=pd.Series(mean3_1990)
	d3_1990=pd.DataFrame(d3_1990)
	d3_1990.columns=['1990.5']
	d3_1990
	#
	thirty_nine_southeastasia_1995=south_east_asia_df['1995.5']
	thirty_nine_southeastasia_1995=thirty_nine_southeastasia_1995.mean()
	thirty_nine_southeastasia_1995
	mean3_1995={'Southeast Asia':thirty_nine_southeastasia_1995}
	d3_1995=pd.Series(mean3_1995)
	d3_1995=pd.DataFrame(d3_1995)
	d3_1995.columns=['1995.5']
	d3_1995
	#
	thirty_nine_southeastasia_2005=south_east_asia_df['2005.5']
	thirty_nine_southeastasia_2005=thirty_nine_southeastasia_2005.mean()
	thirty_nine_southeastasia_2005
	mean3_2005={'Southeast Asia':thirty_nine_southeastasia_2005}
	d3_2005=pd.Series(mean3_2005)
	d3_2005=pd.DataFrame(d3_2005)
	d3_2005.columns=['2005.5']
	d3_2005
	#
	thirty_nine_southeastasia_2000=south_east_asia_df['2000.5']
	thirty_nine_southeastasia_2000=thirty_nine_southeastasia_2000.mean()
	thirty_nine_southeastasia_2000
	mean3_2000={'Southeast Asia':thirty_nine_southeastasia_2000}
	d3_2000=pd.Series(mean3_2000)
	d3_2000=pd.DataFrame(d3_2000)
	d3_2000.columns=['2000.5']
	d3_2000
	#
	thirty_nine_southeastasia_2010=south_east_asia_df['2010.5']
	thirty_nine_southeastasia_2010=thirty_nine_southeastasia_2010.mean()
	thirty_nine_southeastasia_2010
	mean3_2010={'Southeast Asia':thirty_nine_southeastasia_2010}
	d3_2010=pd.Series(mean3_2010)
	d3_2010=pd.DataFrame(d3_2010)
	d3_2010.columns=['2010.5']
	d3_2010
	#
	thirty_nine_southeastasia_2015=south_east_asia_df['2015.5']
	thirty_nine_southeastasia_2015=thirty_nine_southeastasia_2015.mean()
	thirty_nine_southeastasia_2015
	mean3_2015={'Southeast Asia':thirty_nine_southeastasia_2015}
	d3_2015=pd.Series(mean3_2015)
	d3_2015=pd.DataFrame(d3_2015)
	d3_2015.columns=['2015.5']
	d3_2015
	#
	south_east_asia_1=pd.concat([d3_1990,d3_1995,d3_2000,d3_2005,d3_2010,d3_2015],axis=1,join_axes=[d3_1990.index])
	south_east_asia_1
	south_east_asia_1.to_csv('southeaast_asia_1.csv')
	#
	#def westernasia():
	western_asia=['United Arab Emirates','Azerbaijan','Cyprus','Georgia','Iran','Iraq','Jordan','Kuwait','Lebanon','Oman','State of Pakestine','Qatar','Saudi Arabia','Syrian Arab Republic','Turkey','Yemen']
	western_asia_df=thirty_nine_a.loc[thirty_nine_a['Region Name'].isin(western_asia)]
	western_asia_df.to_csv('39_westernasia_data.csv')
	western_asia_df.reset_index(drop=True)
	#
	thirty_nine_westernasia_1990=western_asia_df['1990.5']
	thirty_nine_westernasia_1990=thirty_nine_westernasia_1990.mean()
	thirty_nine_westernasia_1990
	mean4_1990={'Western Asia':thirty_nine_westernasia_1990}
	d4_1990=pd.Series(mean4_1990)
	d4_1990=pd.DataFrame(d4_1990)
	d4_1990.columns=['1990.5']
	d4_1990
	#
	thirty_nine_westernasia_1995=western_asia_df['1995.5']
	thirty_nine_westernasia_1995=thirty_nine_westernasia_1995.mean()
	thirty_nine_westernasia_1995
	mean4_1995={'Western Asia':thirty_nine_westernasia_1995}
	d4_1995=pd.Series(mean4_1995)
	d4_1995=pd.DataFrame(d4_1995)
	d4_1995.columns=['1995.5']
	d4_1995
	#
	thirty_nine_westernasia_2005=western_asia_df['2005.5']
	thirty_nine_westernasia_2005=thirty_nine_westernasia_2005.mean()
	thirty_nine_westernasia_2005
	mean4_2005={'Western Asia':thirty_nine_westernasia_2005}
	d4_2005=pd.Series(mean4_2005)
	d4_2005=pd.DataFrame(d4_2005)
	d4_2005.columns=['2005.5']
	d4_2005
	#
	thirty_nine_westernasia_2000=western_asia_df['2000.5']
	thirty_nine_westernasia_2000=thirty_nine_westernasia_2000.mean()
	thirty_nine_westernasia_2000
	mean4_2000={'Western Asia':thirty_nine_westernasia_2000}
	d4_2000=pd.Series(mean4_2000)
	d4_2000=pd.DataFrame(d4_2000)
	d4_2000.columns=['2000.5']
	d4_2000
	#
	thirty_nine_westernasia_2010=western_asia_df['2010.5']
	thirty_nine_westernasia_2010=thirty_nine_westernasia_2010.mean()
	thirty_nine_westernasia_2010
	mean4_2010={'Western Asia':thirty_nine_westernasia_2010}
	d4_2010=pd.Series(mean4_2010)
	d4_2010=pd.DataFrame(d4_2010)
	d4_2010.columns=['2010.5']
	d4_2010
	#
	#
	thirty_nine_westernasia_2015=western_asia_df['2015.5']
	thirty_nine_westernasia_2015=thirty_nine_westernasia_2015.mean()
	thirty_nine_westernasia_2015
	mean4_2015={'Western Asia':thirty_nine_westernasia_2015}
	d4_2015=pd.Series(mean4_2015)
	d4_2015=pd.DataFrame(d4_2015)
	d4_2015.columns=['2015.5']
	d4_2015
	#
	western_asia_1=pd.concat([d4_1990,d4_1995,d4_2000,d4_2005,d4_2010,d4_2015],axis=1,join_axes=[d4_1990.index])
	western_asia_1
	western_asia_1.to_csv('western_asia_1.csv')
	#
	#def caucacusncentralasia():
	caucasus_n_central_asia=['Armenia','Azerbaijan','Georgia','Kazakhstan','Kyrgyztan','Tajukistan','Turkmenistan','Uzbekistan']
	caucasus_n_central_asia_df=thirty_nine_a.loc[thirty_nine_a['Region Name'].isin(caucasus_n_central_asia)]
	caucasus_n_central_asia_df.to_csv('39_caucasus_data.csv')
	caucasus_n_central_asia_df.reset_index(drop=True)
	#
	thirty_nine_caucacusncentralasia_1990=caucasus_n_central_asia_df['1990.5']
	thirty_nine_caucacusncentralasia_1990=thirty_nine_caucacusncentralasia_1990.mean()
	thirty_nine_caucacusncentralasia_1990
	mean5_1990={'Caucacus and Central Asia':thirty_nine_caucacusncentralasia_1990}
	d5_1990=pd.Series(mean5_1990)
	d5_1990=pd.DataFrame(d5_1990)
	d5_1990.columns=['1990.5']
	d5_1990
	#
	thirty_nine_caucacusncentralasia_1995=caucasus_n_central_asia_df['1995.5']
	thirty_nine_caucacusncentralasia_1995=thirty_nine_caucacusncentralasia_1995.mean()
	thirty_nine_caucacusncentralasia_1995
	mean5_1995={'Caucacus and Central Asia':thirty_nine_caucacusncentralasia_1995}
	d5_1995=pd.Series(mean5_1995)
	d5_1995=pd.DataFrame(d5_1995)
	d5_1995.columns=['1995.5']
	d5_1995
	#
	thirty_nine_caucacusncentralasia_2005=caucasus_n_central_asia_df['2005.5']
	thirty_nine_caucacusncentralasia_2005=thirty_nine_caucacusncentralasia_2005.mean()
	thirty_nine_caucacusncentralasia_2005
	mean5_2005={'Caucacus and Central Asia':thirty_nine_caucacusncentralasia_2005}
	d5_2005=pd.Series(mean5_2005)
	d5_2005=pd.DataFrame(d5_2005)
	d5_2005.columns=['2005.5']
	d5_2005
	#
	thirty_nine_caucacusncentralasia_2000=caucasus_n_central_asia_df['2000.5']
	thirty_nine_caucacusncentralasia_2000=thirty_nine_caucacusncentralasia_2000.mean()
	thirty_nine_caucacusncentralasia_2000
	mean5_2000={'Caucacus and Central Asia':thirty_nine_caucacusncentralasia_2000}
	d5_2000=pd.Series(mean5_2000)
	d5_2000=pd.DataFrame(d5_2000)
	d5_2000.columns=['2000.5']
	d5_2000
	#
	thirty_nine_caucacusncentralasia_2010=caucasus_n_central_asia_df['2010.5']
	thirty_nine_caucacusncentralasia_2010=thirty_nine_caucacusncentralasia_2010.mean()
	thirty_nine_caucacusncentralasia_2010
	mean5_2010={'Caucacus and Central Asia':thirty_nine_caucacusncentralasia_2010}
	d5_2010=pd.Series(mean5_2010)
	d5_2010=pd.DataFrame(d5_2010)
	d5_2010.columns=['2010.5']
	d5_2010
	#
	thirty_nine_caucacusncentralasia_2015=caucasus_n_central_asia_df['2015.5']
	thirty_nine_caucacusncentralasia_2015=thirty_nine_caucacusncentralasia_2015.mean()
	thirty_nine_caucacusncentralasia_2015
	mean5_2015={'Caucacus and Central Asia':thirty_nine_caucacusncentralasia_2015}
	d5_2015=pd.Series(mean5_2015)
	d5_2015=pd.DataFrame(d5_2015)
	d5_2015.columns=['2015.5']
	d5_2015
	#
	caucasus_n_central_asia_1=pd.concat([d5_1990,d5_1995,d5_2000,d5_2005,d5_2010,d5_2015],axis=1,join_axes=[d5_1990.index])
	caucasus_n_central_asia_1
	caucasus_n_central_asia_1.to_csv('caucasus_n_central_asia_1.csv')
	#
	frames = [east_asia_1,south_asia_1,south_east_asia_1,western_asia_1,caucasus_n_central_asia_1]
	final_frames = pd.concat(frames)
	final_frames.to_csv('final_frames.csv')
	final_frames
abc()