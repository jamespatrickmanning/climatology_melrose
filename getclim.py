# routine to get bottom temperature climatology given lat, lon, and day of year
# this is just a example of how it works so it:
# -- assumes today's day of year
# -- assumes hardcoded pos'n 39N, -73.5W
# -- makes a contour map as well with pos'n marked by red dot
import pandas as pd
import numpy as np
from datetime import datetime as dt
from matplotlib import pyplot as plt

dflat=pd.read_csv('/net/data5/jmanning/clim/LatGrid.csv',header=None)
dflon=pd.read_csv('/net/data5/jmanning/clim/LonGrid.csv',header=None)
now=dt.now().strftime('%j')# gets day of year today
lat1=39.0  #hardcoded lat/lon for demo purposes
lon1=-73.5

bt=pd.read_csv('/net/data5/jmanning/clim/Bottom_Temperature/BT_'+now+'.csv',header=None) # gets bottom temp for this day of year
btmap=plt.contourf(dflon,dflat,bt) # contour fills 
plt.colorbar(btmap)
plt.plot(lon1,lat1,'r.') # marks the position with red dot
plt.show()
lat=np.array(dflat[0])   # gets the first col (35 to 45)
lon=np.array(dflon.ix[0])# gets the first row (-75 to -65)
idlat = np.abs(lat - lat1).argmin()
idlon = np.abs(lon - lon1).argmin()
print bt[idlon][idlat] # prints temp to screen

