import numpy as np
import pandas as pd
import xarray as xr

# create temprtre data
np.random.seed(123)
size = 4
temperature = 15 + 10 * np.random.randn(size)  # don't like lack of ()s
lat = np.random.uniform(low=-90, high=90, size=size)
lon = np.random.uniform(low=-180, high=180, size=size)

# 2 digits decimal rounding
temperature, lat, lon = np.around([temperature, lat, lon], decimals = 2)

# reprsnt in PANDAS
df = pd.DataFrame({'temperature':temperature, 'lat':lat, 'lon':lon})
print(f"\nDataFrame::\n{df}")

# create DataArray from SERIES
# 2 dimesions in our data, so use 2LEVEL-multi-index::
idx = pd.MultiIndex.from_arrays(arrays=[lat, lon], names=['lat', 'lon'])

ser = pd.Series(data=temperature, index=idx)
print(f"\nSeries::\n{ser}")

# 'use from_series method'
darr = xr.DataArray.from_series(ser)
print(f"\nDataArray::\n{darr}")

# create DataArray from DATAFRAME
# deflt the index of DF is the 1st dim & cols as the 2nd dim
# NESTED-DIM's created if <index> or <cols> have MULITPLE LEVELS

# PIVOT the df to get appropriate DIM's imported
df_pv = df.pivot(index='lat', columns='lon')

# drop 1st level of cols, b/c not necessary
df_pv = df_pv.droplevel(0, axis=1)   # don't understand this function

print(f"\nDF-pivoted::\n{df_pv}")