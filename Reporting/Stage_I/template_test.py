import pandas as pd
import numpy as np

from bokeh.plotting import figure, output_file, show

x_axis = [-4, -2, -1, 0, 5, 16, 17, 18, 91]
y_axis = [11, 12, 13, 14, 15, 16, 17, 18, 19]

output_file('test2.html')

# plot

p = figure(
    title='My first Bokeh report  !',
    x_axis_label="X",
    y_axis_label="Y"
)
# render

p.line(x_axis,y_axis, legend = 'KROKAKAKOPUCHILA !!! ', line_width = 2)
show(p)
