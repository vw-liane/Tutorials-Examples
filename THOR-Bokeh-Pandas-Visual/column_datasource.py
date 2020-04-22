# bokeh object ColumnDataSource has DataFrame as an argument
# then CDS-obj passes to GLYPH methods with 'source' param
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

# QUANITATIVE DATA plotted here
output_file('columndatasource_example.html') # best practice at BEGIN of file
df = pd.read_csv('thor_wwii.csv')

sample = df.sample(50)  # random 50-row sample
source = ColumnDataSource(sample)

p = figure()  # of type PLOT
p.circle(x='TOTAL_TONS', y='AC_ATTACKING', # call circle glyph to plot data
         source=source, size=10, color='green')

# can also give column_names for <size>, <line_color> or <fill_color>
# size='TONS_HE'

p.title.text = "Attacking Aicraft and Munitions Dropped"   # add title
p.xaxis.axis_label = "Tons of Munitions Dropped"           # label axes
p.yaxis.axis_label = "Number of Attacking Aircraft"

# BEGIN CUSTOMIZABLE-INTERACTIVE facets of plots
# can add more tools to the toolbar
hover = HoverTool()                 # useful for explore & interct w/ DATA
hover.tooltips=[   # ('Display Name', '@COLUMN_NAME')
    ('Attack Date', '@MSNDATE'),
    ('Attacing Aircraft', '@AC_ATTACKING'),
    ('Tons of Munitions', '@TOTAL_TONS'),
    ('Type of Aircraft', '@AIRCRAFT_NAME')
]
p.add_tools(hover)
show(p)              # output to HTML file