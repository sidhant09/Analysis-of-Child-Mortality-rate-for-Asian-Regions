import pandas as pd
import numpy as np

def abc():
	df = pd.read_excel('40a.xlsx')
	df1 = pd.DataFrame(df)
	df1.to_csv('40a.csv')
	csv_file = pd.read_csv('40a.csv')
	selected_columns_40a=csv_file[['ISO Codes','Region Name','Uncertainity bounds','1990.5','1991.5','1992.5','1993.5','1994.5','1995.5','1996.5','1997.5','1998.5','1999.5','2000.5','2001.5','2002.5','2003.5','2004.5','2005.5','2006.5','2007.5','2008.5','2009.5','2010.5','2011.5','2012.5','2013.5','2014.5','2015.5']]
	list(selected_columns_40a)
	forty_a=pd.DataFrame(selected_columns_40a)
	#.to_csv('40a.csv')

	def east_asia():
		#east_asia_df = pd.read_csv('40a.csv')
		east_asia=['China','Japan','Republic of Korea','Mongolia',"Democratic People's Republic of Korea"]
		east_asia_df=forty_a.loc[forty_a['Region Name'].isin(east_asia)]
		east_asia_df.to_csv('40a_1.csv')
	#east_asia_df.reset_index(drop=True)
	#
	def south_asia():
		south_asia_df = pd.read_csv('40a.csv')
		south_asia=south_asia=['Afghanistan','Bangladesh','Bhutan','India','Sri Lanka','Maldives','Nepal','Pakistan']
		south_asia_df=forty_a.loc[forty_a['Region Name'].isin(south_asia)]
		south_asia_df.to_csv('40a_2.csv')
	#south_asia_df.reset_index(drop=True)
	#
	def south_east_asia():
		south_east_asia=['Brunei Darussalam','Indonesia','Cambodia','Myanmar','Malaysia','Philippines','Singapore','Thailand','Timor-Leste','Viet Nam']
		south_east_asia_df=forty_a.loc[forty_a['Region Name'].isin(south_east_asia)]
		south_east_asia_df.to_csv('40a_3.csv')
	#south_east_asia_df.reset_index(drop=True)
	#
	def western_asia():
		western_asia=['United Arab Emirates','Azerbaijan','Cyprus','Georgia','Iran','Iraq','Jordan','Kuwait','Lebanon','Oman','State of Pakestine','Qatar','Saudi Arabia','Syrian Arab Republic','Turkey','Yemen']
		western_asia_df=forty_a.loc[forty_a['Region Name'].isin(western_asia)]
		western_asia_df.to_csv('40a_4.csv')
	#western_asia_df.reset_index(drop=True)
	#
	def caucasus_n_central_asia():	
		caucasus_n_central_asia=['Armenia','Azerbaijan','Georgia','Kazakhstan','Kyrgyztan','Tajukistan','Turkmenistan','Uzbekistan']
		caucasus_n_central_asia_df=forty_a.loc[forty_a['Region Name'].isin(caucasus_n_central_asia)]
		caucasus_n_central_asia_df.to_csv('40a_5.csv')
	#caucasus_n_central_asia_df.reset_index(drop=True)
	#
	def east_asia_exchina():	
		east_asia_exchina=['Japan','Republic of Korea','Mongolia',"Democratic People's Republic of Korea"]
		east_asia_exchina_df=forty_a.loc[forty_a['Region Name'].isin(east_asia_exchina)]
		east_asia_exchina_df.to_csv('40a_5.csv')
	#east_asia_exchina_df.reset_index(drop=True)
	#
	def south_asia_exindia():	
		south_asia_exindia=['Afghanistan','Bangladesh','Bhutan','Sri Lanka','Maldives','Nepal','Pakistan']
		south_asia_exindia_df=forty_a.loc[forty_a['Region Name'].isin(south_asia_exindia)]
		south_asia_exindia_df.to_csv('40a_6.csv')
	#south_asia_exindia_df.reset_index(drop=True)

	east_asia()
	south_asia()
	south_east_asia()
	western_asia()
	east_asia_exchina()
	south_asia_exindia()
abc()