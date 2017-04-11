import pandas as pd
import nvd3
from IPython.display import Image
from IPython.core.display import display, HTML
from nvd3 import lineChart
#
df = pd.read_excel(r"/home/sidhant/pro_new/pen_2/final_2/pivot_ic.xlsx")
df = pd.DataFrame(df)
#
output_file = open('india_vs_china.html', 'w')
chart = lineChart(width = 1000,name="lineChart", x_is_date=False, x_axis_format=None)
#
xdata = df['Year']
y1 = df['India']
y2 = df['China']
#
extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=y1, x=xdata, name='India', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=y2, x=xdata, name='China', extra=extra_serie)
#
chart.set_containerheader("<h2>Child Mortality rate for China and India from 1990.5 to 2015.5<h2>")
chart.buildhtml()
display(HTML(chart.htmlcontent))
output_file.write(chart.htmlcontent)
output_file.close()