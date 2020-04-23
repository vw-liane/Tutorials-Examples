import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d
from bokeh.layouts import layout
from bokeh.palettes import Spectral3
from bokeh.tile_providers import CARTODBPOSITRON    # tile providers for base maps of world
from pyproj import Proj, transform

output_file('mapping_targets.html')

## CORRDINATE SYS & MAPPING PROJECTION
######################################
# helper function to convert lat/long to easting/northing for mapping
# ... relies on funtions from <PYPROJ> library
def LongLat_to_EN(long, lat):
    try:          # '+init=<authority>:<code>' syntax is deprecated
                  # <authority>:<code> is preferred initialization method
        easting, northing = transform(
            Proj(init='epsg:4326'), Proj(init='epsg:3857'), long, lat)
        return easting, northing
    except:
        return None, None

df = pd.read_csv('thor_wwii.csv')

# helper to convert all lat/ong to webmercator and stores in new column
# load data & apply conversion, create new columns
df['E'], df['N'] = zip(*df.apply(lambda x: LongLat_to_EN(x['TGT_LONGITUDE'], x['TGT_LATITUDE']), axis=1))
## END COOR/ PROJ
################

# group data by 'E' & 'N' to get UNIQUE target locations       # <res...indx()> keeps 'E', 'N' as columns
grouped = df.groupby(['E', 'N'])['TONS_IC', 'TONS_FRAG'].sum().reset_index()

filter = grouped['TONS_FRAG'] != 0
grouped = grouped[filter]        # get rows with NOT-0 values in DF

source = ColumnDataSource(grouped)

# set bounds
left = -2150000
right = 18000000
bottom = -5300000
top = 11000000
            # set mins & maxs                 # <Range1D> for 1-dim data
p = figure(x_range=Range1d(left,right), y_range=Range1d(bottom, top))

p.add_tile(CARTODBPOSITRON)
p.circle(x='E', y='N', source=source, )

p.xaxis.visible = False

show(p)