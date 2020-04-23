import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
output_file('simple_timeseries_plot.html')

df = pd.read_csv('thor_wwii.csv')

# make sure MSNDATE is <datetime> format      # <format> makes process faster
df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format='%m/%d/%Y')

grouper_obj = pd.Grouper(key='MSNDATE', freq='M')   # <freq='2W' for two week interval resampling
grouped = df.groupby(grouper_obj)['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
grouped = grouped / 1000      # into kilotons

source = ColumnDataSource(grouped)

p = figure(x_axis_type='datetime')  # x data wil be datetimes

p.line(x='MSNDATE', y='TOTAL_TONS', line_width=2, source=source, legend='All Munitions')
p.line(x='MSNDATE', y='TONS_FRAG', line_width=2, source=source, color=Spectral3[1], legend='Fragmentation')
p.line(x='MSNDATE', y='TONS_IC', line_width=2, source=source, color=Spectral3[2], legend='Incendiary')

p.yaxis.axis_label = "Kilotons of Munitions Dropped"

show(p)