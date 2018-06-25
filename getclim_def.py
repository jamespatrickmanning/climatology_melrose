# routine to get climatology given lat, lon, yearday
import pandas as pd
import numpy as np
from datetime import datetime as dt
import glob
from conversions import dm2dd
def getclim(lat1=43.,lon1=-73.0,yrday=dt.now().strftime('%j'),var='Bottom_Temperature/BT_'): 
  # gets climatology of Bottom_Temperature, Surface_Temperature, Bottom_Salinity, or Surface_Salinity
  # as calculated by Chris Melrose from 30+ years of NEFSC CTD data on the NE Shelf 
  # where "lat1", "lon1", and "yrday" are the position and yearday of interest
  # where "var" is the variable of interest (usually Bottom_Temperature) 
  inputdir='/net/data5/jmanning/clim/' # hardcoded climatology directory name "/home/pi/clim/"
  inputdir_csv='/net/data5/jmanning/li/Matdata/temporary/' # the csv files that have lat/lon "/home/pi/towifi/"
  dflat=pd.read_csv(inputdir+'LatGrid.csv',header=None)
  dflon=pd.read_csv(inputdir+'LonGrid.csv',header=None)
  lat=np.array(dflat[0])   # gets the first col (35 to 45)
  lon=np.array(dflon.ix[0])# gets the first row (-75 to -65)
  clim=pd.read_csv(inputdir+var+yrday+'.csv',header=None) # gets bottom temp for this day of year
  print lat1,lon1
  if lat1==43.:
    files=sorted(glob.glob(inputdir_csv+'*.csv')) # gets all the csv files in the towfi directory
    dfcsv=pd.read_csv(files[-1],sep=',',skiprows=7)
    [lat1,lon1]=dm2dd(float(dfcsv['lat'][0][0:-1]),float(dfcsv['lon'][0][0:-1]))
  print lat1,lon1
  idlat = np.abs(lat - lat1).argmin() # finds the neareast lat to input lat1
  idlon = np.abs(lon - lon1).argmin() # finds the neareast lon to input lon1
  return clim[idlon][idlat]
# test function:
result=getclim()#43.,-70.)
print result
result=getclim(43.1,-69.)
print result

