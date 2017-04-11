import pandas as pd
import nvd3
from nvd3 import multiBarChart
from IPython.display import Image
from IPython.core.display import display, HTML
#
output_file = open('china.html', 'w')
chart = multiBarChart(width=1250, height=400, x_axis_format=None,color = 'blue')
xdata = ['1990.5','1995.5','2000.5','2005.5','2010.5','2015.5']
ylower = [49.6, 44.8, 34.9, 22.5, 14.7, 9]
ymedian = [53.8, 47.5, 36.9, 24, 15.7, 10.7]
yupper= [58.8, 50.4, 39.2, 25.5, 16.7, 12.7]
chart.add_serie(name="Upper", y=yupper, x=xdata)
chart.add_serie(name="Median", y=ymedian, x=xdata)
chart.add_serie(name="Lower", y=ylower, x=xdata)
chart.set_containerheader("<h2>Child Mortality rate for China from 1990.5 to 2015.5<h2>")
chart.buildhtml()
display(HTML(chart.htmlcontent))
output_file.write(chart.htmlcontent)
output_file.close()