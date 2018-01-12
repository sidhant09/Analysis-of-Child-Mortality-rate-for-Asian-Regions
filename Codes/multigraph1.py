import pandas as pd
import nvd3
from nvd3 import multiBarChart
from IPython.display import Image
from IPython.core.display import display, HTML
df = pd.read_excel(r"/home/sidhant/pro_new/pen_2/final_2/40/pivot_total.xlsx")
df = pd.DataFrame(df)
output_file = open('asia.html', 'w')
chart = multiBarChart(width=1100, height=400, x_axis_format=None,color = 'green')
xdata = df['Year']
ylower = df['East Asia']
ymedian = df['South Asia']
yupper= df['Southeast Asia']
ytop=df['Western Asia']
ybottom=df['Caucacus and Central Asia']
chart.add_serie(name="East Asia", y=ylower, x=xdata)
chart.add_serie(name="South Asia", y=ymedian, x=xdata)
chart.add_serie(name="Southeast Asia", y=yupper, x=xdata)
chart.add_serie(name="Western Asia", y=ytop, x=xdata)
chart.add_serie(name="Caucacus and Central Asia", y=ybottom, x=xdata)
chart.set_containerheader("<h2>Estimate child deaths in Asian regions from 1990.5 to 2015.5 (in thousands)")
chart.buildhtml()
display(HTML(chart.htmlcontent))
output_file.write(chart.htmlcontent)

# close Html file
output_file.close()