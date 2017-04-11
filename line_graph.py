import pandas as pd
import nvd3
from IPython.display import Image
from IPython.core.display import display, HTML
from nvd3 import lineChart
#
df = pd.read_excel(r"/home/sidhant/pro_new/pen_2/final_2/asia_pivot.xlsx")
df = pd.DataFrame(df)
#
df1 = pd.read_excel(r"/home/sidhant/pro_new/pen_2/final_2/pivot_39c.xlsx")
df1 = pd.DataFrame(df1)


output_file = open('asia_linegraph.html', 'w')
chart = lineChart(width = 1000,name="lineChart", x_is_date=False, x_axis_format=None)
#
xdata = df['Year']
y1 = df['East Asia']
y2 = df['South Asia']
y3= df['Southeast Asia']
y4= df['Western Asia']
y5= df['Caucacus and Central Asia']
y6= df1['Eastern Asia excluding China']
y7= df1['Southern Asia excluding India']
#
extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=y1, x=xdata, name='Eastern Asia', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y2, x=xdata, name='Southern Asia', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y3, x=xdata, name='Southeast Asia', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y4, x=xdata, name='Western Asia', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y5, x=xdata, name='Caucacus and Central Asia', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y6, x=xdata, name='Eastern Asia excluding China', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y7, x=xdata, name='Southern Asia excluding India', extra=extra_serie)
#
chart.set_containerheader("<h2>Child Mortality rate for Asian regions from 1990.5 to 2015.5<h2>")
chart.buildhtml()
display(HTML(chart.htmlcontent))
output_file.write(chart.htmlcontent)
output_file.close()