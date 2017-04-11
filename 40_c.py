import pandas as pd
import numpy as np

def abc():
	df = pd.read_excel('40c.xlsx')
	df1 = pd.DataFrame(df)
	df1.to_csv('40c.csv')
	csv_file = pd.read_csv('40c.csv')
	selected_columns_40c=csv_file[['Region Name','Uncertainity bounds','1990.5','1991.5','1992.5','1993.5','1994.5','1995.5','1996.5','1997.5','1998.5','1999.5','2000.5','2001.5','2002.5','2003.5','2004.5','2005.5','2006.5','2007.5','2008.5','2009.5','2010.5','2011.5','2012.5','2013.5','2014.5','2015.5']]
	#list(selected_columns_39a)
	forty_c=pd.DataFrame(selected_columns_40c)
	#
	region=['Developed Region','Developing Region','Northern Africa','Sub-Saharan Africa','Latin America and The Carribean','Eastern Asia','Eastern Asia excluding China','Southern Asia excluding India','Western Asia','Oceania','World'] 
	region_df=forty_c.loc[forty_c['Region Name'].isin(region)]
	#region.reset_index(drop=True)

abc()