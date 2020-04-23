# focus on USA & Britain who by far had the most
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3        # this time 3-color Spectral palette
output_file('types_of_munitions.html')

df = pd.read_csv('thor_wwii.csv')

# exclude records that don't include 'USA' or 'GREAT BRITAIN'
#  ** <.isin> checks with C-F-M has value .... T or F values
# ... rows with <False> values are discarded
filter = df['COUNTRY_FLYING_MISSION'].isin(('USA', 'GREAT BRITAIN'))
df = df[filter]

grouped = df.groupby('COUNTRY_FLYING_MISSION')['TONS_IC', 'TONS_FRAG', 'TONS_HE'].sum()
grouped = grouped / 1000    # convert tons to kilotons

source = ColumnDataSource(grouped)    # create source object
countries = source.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=countries)         # set categorical data for x-axis

p.vbar_stack(stackers=['TONS_HE', 'TONS_FRAG', 'TONS_IC'],     # order matters
             x='COUNTRY_FLYING_MISSION', source=source,        # glyph method
             legend = ['High Explosive', 'Fragmentation', 'Incendiary'],
             width=0.5, color=Spectral3)

p.title.text = "Types of Munitions Dropped by Allied Country"
p.legend.location = 'top_left'

p.xaxis.axis_label = "Country"
p.xgrid.grid_line_color = None    # no x-grid lines

p.yaxis.axis_label = "Kilotons of Munitions"

show(p)
