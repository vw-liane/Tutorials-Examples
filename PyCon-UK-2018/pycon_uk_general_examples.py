import numpy as np
import xarray as xr 
# .. import datetime ..

# standard 3-dim  random numpy-array w/ 3 DIMs
arr = np.random.rand(3, 4, 2)
new_arr = xr.DataArray(arr)
print(f"The simple np-array MADE XARR::\n{new_arr}")
# output:: <xarray.DataArray (dim_0: 3, dim_1: 4, dim_2: 2)>
# looks like only NP array

# but if give more metadata, can do more powerful things
better_arr = xr.DataArray(arr, dims='x', 'y', 'time'))
# !! now can call mean over 'time' instead of foreign 'axis=2'
print(f"XARR-DataArray:\n{better_arr}")
# output:: xarray.DataArray (x: 3, y:4, time:2)>
# ... BUT! still has DIMs w/o coordinates


# so pass a <coords> dictionary
new_da = xr.DataArray(arr, 
                dims=('x', 'y', 'time'),
                coords={'x': [10, 20, 30],
                        'y': [0.3, 0.7, 1.3, 1.5],
                        'time': {[datetime.datetime(2016, 3, 5),
                                  datetime.datetime(2016, 4, 7)]} )
print(f"Full Contents::\n{new_da}")
# output:: <xarray.DataArray (x: 3, y: 4, time:2)>
# Coordinates:
# * x       (x) int64 10 20 30
# * y       (y) float64 0.3 0.7 1.3 1.5
# * time    (time) datetime64[ns] 2016-03-05 2016-04-07                 
# ^^ lists content, coords, length of DIMs


# some stuff we can do ... select using names indices
print(f"March-05-2016::\n{new_da.sel(time='2016-03-05')}")
# output:: <xarray.DataArray (x:3, y: 4)>
#    Coordinates:
# * x       (x) int64 10 20 30
# * y       (y) float64 0.3 0.7 1.3 1.5
#  time    (time) datetime64[ns] 2016-03-05  
## .. ^^no asterisk means is ACTIVE, VARYING coordinate


# can also use <isel> function ... which is <index-selection>
print(f"Selected <time=1>:\n{new_da.isel(time=1)}") # claro 2nd elem
# output:: <xarray.DataArray (x:3, y:4)>
#    Coordinates:
# * x       (x) int64 10 20 30
# * y       (y) float64 0.3 0.7 1.3 1.5
#  time    (time) datetime64[ns] 2016-04-07  


# can do slices
print(f"X-sliced 0 to 20::\n{new_da.sel(x=slice(0, 20))}")
# output:: <xarray.DataArray (x:2, y:4, time:2>
#    Coordinates:
# * x       (x) int64 10 20 30
# * y       (y) float64 0.3 0.7 1.3 1.5
# * time    (time) datetime64[ns] 2016-03-05 2016-04-07  


# apply arithmetic & reduction operators
print(f"Show Time Mean::\n{new_da.mean(dim='time')}")
# output:: <xarray.DataArray (x:3, y:4)>
#      3 x 4 array (lines x cols)
# * x       (x) int64 10 20 30
# * y       (y) float64 0.3 0.7 1.3 1.5


# mean over multiple DIMs at once
print(f"Mean over <x> & <y> axes::\n{new_da.mean(dim=['x', 'y'])}")
# output:: xarray.DataArray (time:2)>
#      1 x 2 array ... across whole image for each time-step
#     Coordinates:
# * time    (time)datetime64[ns] 2016-03-05 2016-4-07


# MULTIPLE actions in one line
# ... sel ... groupby ... std
print(f"Select Year 2014, GroupBy Month, take StandardDev::")
print(f"{PM25.sel(time='2014').groupby('time.month').std(dim='time')}")
# output:: <xarray.DataArray 'data' (month: 6, y: 1162, x:1240)>
#  Coordinates ...
# * y      (y) float64 1.429e+06 ... ...  
# * x ...  (x) float64 -9.476e+05 ... ...
# * month  (month) int64 1 2 3 4 5 6    # only 6 months of data
        


