# interpolation .. 

# at particular x & y location
# converting to pandas DF, dropping empty
# ? default bicubic interpolation of surrnding pixels
PM25.interp(x=318193.5, y=176849.7).to_pandas().dropna().head()

# or same but with CLOSEST pixels to this location
PM25.interp(x=318193.5, y=176849.7, method='nearest').to_pandas().dropna().head()


# RESAMPLE time series ... what like on average in Januarys, Febs, etc
# same code as in Pandas
PM25.resample(time='1M').mean(dim='time')

# rolling windows over time
PM25.rolling(time=5).mean()

# OPeNDAP
# access large vols of data over internet, but only 
# ... download parts we need
# opens NETCDF file over HTTP connection
dataset = xr.open_dataset('http://opendap.knmi.nl/knmi/thredds/dodsC/e-obs
            _0.25regular/tg_0.25deg_reg_v17.0.nc')

# only takes metadata at beginn...w/o downloading whole file
           
# check dataset   (mulitiple data arrays within it)
print(dataset['tg'])     
# can see what attributes are like mean-etc    



# select data in 2019 and plot it
## ONLY DATA FOR THIS PLOT
temperature = dataset['tg']
oneday = temperature.sel(time='2009-07-01')
oneday.plot(robust=True)
# output <matplotlib.collections.QuadMesh at ... >   




# XARRAY EXTENSIONS! #
# simulation models with <xarray-simlab>
# WRF Weather Forecasting Model functions (wrf-python)
# EMPIRICAL ORTHOGONAL functiosn (eofs)
# ... and MORE! @ Xarray site on FAQ "what other projects leverage xarray")
#         ^^^^^^^^check this out!!^^^^^^^^

from eofs.xarray import Eof
monthly = PM25.resample(time='M').mean('time')
solver = Eof(monthly)
results = solver.eofs()
results.plot(col='mode',col_wrap=3, robust=True)
# output <xarray.plot.facetgrid.FacetGrid at ... >


# RESOURCES .. **
# slides: http://bit.do/xarray_pyconuk
# code: https://github.com/robintw/XArray_PyConUK2018
# Xarray dos: http://xarray.pydata.org/
#   robin@rtwilson.com   @sciremotesense    @robintw on Slack
