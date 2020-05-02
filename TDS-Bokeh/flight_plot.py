# older version of bokeh used
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool
output_file('flight_plot.html')

# into DF
flights_df = pd.read_csv('flights.csv', index_col=0)

# summary stats for the ARR_DELAY col
print(f"arr_delay column info::\n{flights_df['arr_delay'].describe()}\n")

# histogram will show distribution of data
# x is the variable grouped into bin-intervals -- delay in MINutes
# y (height) is num of data points in interval -- num of flights
## use the QUAD GLYPH ... specify each edge of bar

### Bins-width = 5 min
### num-bins =  (length of interval / 5).
### Limit delays to [-60, +120] minutes using the range.
arr_hist, edges = np.histogram(flights_df['arr_delay'],
                               bins= int(180/5), range=[-60, 120])
# put info into DF
delays_df = pd.DataFrame({'flights': arr_hist,
                          'left': edges[:-1], 'right': edges[1:]})
print(delays_df)

# make new figure, & add QUAD glyph
p = figure(plot_height = 600, plot_width = 600, title='Arrival Delays Histogram',
           x_axis_label='Minutes of Delay', y_axis_label='Number of Flights')

#p.quad(bottom=0, top=delays_df['flights'], left=delays_df['left'], right=delays_df['right'],
#       fill_color='red', line_color='black')

## for TOOLTIPS, need to change source from DF INTO ColumnDataSource
## CDS is plotting object w/ data, methods and attributes
## CDS allows ANNOTATIONs & INTERACTIVITY

# ... add passive inspectors ...
source = ColumnDataSource(delays_df)
#print(f"CDS Keys::\n{source.data.keys}")  # supposed to show the col-keys as 'flights','left','right','index'

# new way of referencing COLS directly by STRINGS
# add quad glype, w/ SOURCE
p.quad(source=source, bottom=0, top='flights', left='left', right='right',
       fill_color='red', line_color='black')

# pass hovertool-obj a list of TOOLTIPS as <tuple>s
# tuple -- (label-for-data, spec-data-to-focus-on)
# '@' for pointat our data ... '$' for posit on graph

# or hov = HoverTool() -\n- hov.tooltips= ...
hov = HoverTool(tooltips = [('Delay Interval Left', '@left'),  #'Delay', '@f_interval'
                            ('(x, y)', '($x, $y)')])          # 'Nun of Flights', '@f_flights'

## # Add a column showing the extent of each interval
# not well explained
##delays['f_interval'] = ['%d to %d minutes' % (left, right)
##    for left, right in zip(delays['left'], delays['right'])]

hov.mode = "vline"
p.add_tools(hov)

show(p)