import pandas as pd
import nvd3
from nvd3 import multiBarChart
from IPython.display import Image
from IPython.core.display import display, HTML
#
output_file = open('india.html', 'w')
chart = multiBarChart(width=1300, height=400, x_axis_format=None,color = 'blue')
xdata = ['1990.5','1995.5','2000.5','2005.5','2010.5','2015.5']
ylower = [121.6, 105, 88, 71.6, 56.6, 42.4]
ymedian = [125.8, 108.7, 91.2, 74.6, 59.9, 47.7]
yupper= [130.1, 112.7, 94.7, 77.9, 63.4, 53.3]
chart.add_serie(name="Upper", y=yupper, x=xdata)
chart.add_serie(name="Median", y=ymedian, x=xdata)
chart.add_serie(name="Lower", y=ylower, x=xdata)
chart.set_containerheader("<h2>Child Mortality rate for India from 1990.5 to 2015.5<h2>")
chart.buildhtml()
chart.buildhtml()
display(HTML(chart.htmlcontent))
output_file.write(chart.htmlcontent)
output_file.close()