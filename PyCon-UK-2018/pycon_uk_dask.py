import xarray as xr

# EFFIC PROCSSNG with <dask> && <dask.distributed>
# can open a multifile dataset ... <mfdataset>
                        # two NETCDF files
data = xr.open_mfdataset(['DaskTest1.nc', 'DaskTest2.nc'], 
                        chunks={'time':10})['data']
                         # ^^ 10-time step chunks at a time
# take average over time
avg = data.mean(dim='time')  

## we can read the execution graph created in DASK
# rectangles are for DATA   
# circles are for FUNCTIONS
# ... walks up from two files in btm of screen
# ... get data from each chunk ...
## .. two processing chains are entirely INDEPENDENT until top ...
##  means can run on separate computers, cores, etc, ways to run in parallel!!
                

# a little more complicated
seasonal = data.groupby('time.season').mean(dim='time')                
## more complicated graph .... but can still see separate proessing chains
# .. can see shared data that is loaded only once
# be careful with interactions b/w the chains
# still can be run in separate cores, computers for max-efficiency

### DASK.DISTRIBUTED
# way to run things on multiple computers
# ... colored chunks are different tasks being run on computers
# white gaps is when not running something

# DASK is its own thing ... can use dask-arrays instead of xarray
# ... can us dask-dataframe instead of Pandas dataframe
# ... but is built into Xarray for ease of use


# HOW read DATA into Xarray??
# various formats directly ... NETCDF, HDF, GRIB
# presenter's geographic satellite data 
#    ^^^ so convenient to use Xarray's <rasterio> modul to read
#             GEOgraphic RASTER FORMATS
# simple fnctn
print(f"Open as raster::\n{xr.open_rasterio('satellite_image.tif')}")
# ... output ...
# interestin coordinates ... "band" colors, wavelengths
# y & x coordinates from geographic referencin of the file's metadata of global location
#                   ^^ eastings and northings
## easily customizable and parsable ATTRIBUTES



# EXAMPLE ... thousands of image files want to combine into Xarray
# put into array with time DIM
def fil_to_da(fliename):
    da = xr.open_rasterio(filename)
    
    time_str = os.path.basename(filename)[17:-17]  # time from filename
    time_obj = datetime.datetime.strptime(time_str, '%Y%j%H%M')
    da.coords['time'] = time_obj
    
    return da.isel(band=0)
    
# list comprehension to fun for every file in directory
list_of_data_arrays = [fil_to_da(filename) for filename in files]

# concatenate over time
combined_over_time = xr.concat(list_of_data_arrays, dim='time')
# VOILA!! have multidimensional Xarray

print(f"The shape: {combined_over_time.shape}")
print(f"See coords:\n{combined_over_time.coords}")



# getting RASTER data our of XARRAY in geographic format for GIS & other systems
from xarray_to_rasterio import xarray_to_rasterio  # presenter's OG library
mean = combined.mean(dim='time', keep_attrs=True)
# send to tif
xarray_to_rasterio(mean, 'Mean.tif')