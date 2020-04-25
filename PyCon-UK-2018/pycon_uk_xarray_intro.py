import xarray as xr
                        # their directory obvsly
PM25 = xr.open_dataarray('/Users/robin/code/MAIACProcessing/A112014.nc')
                        # netcdf
# has shape like numpy array
print(f"DARR Shape:: {PM25.shape}")
# output: (181, 1162, 1240)

# *BUT* also has names for dims
print(f"DARR Dim-names: {PM25.sims}")

# make a grouping over season, averaging time
seasonal = PM25.groupby('time.season').mean(dim='time')) #rest-line-cut-off
season.plot.imshow(col='season', robust=True)
# output is xarray.plot.facetgrid.FaceGrid at ...

# get prtclr location with <DARR.isel()> function    # drop missing data
time_series = PM25.isel(x=1000, y=1100).to_pandas().dropna()   
print(f"Time Series::\n{time_series})
                     
                     
# open an image with a particular date
one_day = PM25.sel(time='2014-02-15')
one_day.plot(robuts=True)
# output:: <matplotlib.collections.QuadMesh at ... >                     