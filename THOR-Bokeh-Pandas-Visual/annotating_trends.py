import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from datetime import datetime
from bokeh.palettes import Spectral3
from bokeh.models import BoxAnnotation     #  highlight recognized trends in chart

output_file('eto_operations.html')

df = pd.read_csv('thor_wwii.csv')

# filter for European Theater of Operations
filter = df['THEATER']=='ETO'
df = df[filter]

df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format='%m/%d/%Y')
grouper_obj = pd.Grouper(key='MSNDATE', freq='M')
group = df.groupby(grouper_obj)['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
group = group / 1000   # kilotons convrsn

source = ColumnDataSource(group)

p = figure(x_axis_type="datetime")

p.line(x='MSNDATE', y='TOTAL_TONS', line_width=2, source=source, legend='All Munitions')
p.line(x='MSNDATE', y='TONS_FRAG', line_width=2, source=source, color=Spectral3[1], legend='Fragmentation')
p.line(x='MSNDATE', y='TONS_IC', line_width=2, source=source, color=Spectral3[2], legend='Incendiary')

p.title.text = 'European Theater of Operations'

p.yaxis.axis_label = 'Kilotons of Munitions Dropped'

# BEGIN ANNOTATIONS ON CERTAIN SECTIONS
# create box for annot. decide coordintes.
# ... can be position relating to data or w/ screen units (one place)

# to_datetime() works with month-,day- & year-FIRST formats!
box_left = pd.to_datetime('6-6-1944')  # left side is D-Day
box_right = pd.to_datetime('16-12-1944')  # right side is first of Battle of Bulge

# constuctor & styling arguments
box = BoxAnnotation(left=box_left, right=box_right,
                    line_width=1, line_color='black', line_dash='dashed',
                    fill_alpha=0.2, fill_color='orange')
p.add_layout(box)   # add to the PLOT figure

show(p)