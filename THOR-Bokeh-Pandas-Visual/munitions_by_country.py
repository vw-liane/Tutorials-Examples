import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

from bokeh.palettes import Spectral5   # five-color pallette of many
from bokeh.transform import factor_cmap   # helper method for mppng colrs in bar-charts

# CATEGORICAL DATA plotted here
output_file('munitions_by_country.html')
df = pd.read_csv('thor_wwii.csv')

# new DF output                                # aggregating methods for how to group them
grouped = df.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_HE', 'TONS_IC', 'TONS_FRAG'].sum()
                                              # also exists <count> <mean> <max> <min>

print(grouped)  # note error in South Africa & New Zealand first two COL #s

grouped = grouped / 1000 # convert to kilotons? how works?

source = ColumnDataSource(grouped)
countries = source.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=countries)   # tell figure how to handle the x-axis
                                # auto-categorical because list is TEXT data
# indiv-colored bars per each FACTOR (category)
color_map = factor_cmap(field_name='COUNTRY_FLYING_MISSION',
                        palette=Spectral5, factors=countries)

p.vbar(x='COUNTRY_FLYING_MISSION', top='TOTAL_TONS', source=source, width=0.70, color=color_map)

p.title.text = "Munitions Dropped by Allied Country"
p.xaxis.axis_label = "Country"
p.yaxis.axis_label = "Kilotons of Munitions"

hover = HoverTool()            # multiple data variables in a single line
hover.tooltips = [ ("Totals", "@TONS_HE High Explosive / @TONS_IC Incendiary / @TONS_FRAG Fragmentation") ]

hover.mode = "vline"    # programs WHEN to POPUP (if mouse cross a vline in bar)
p.add_tools(hover)
show(p)