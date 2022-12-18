import pandas as pd
import math
import numpy as np

data=pd.read_excel("hub.xlsx",sheet_name="Sheet1")

def hub_finder(df,lon2,lat2):

    def haversine_vectorize(lon1, lat1, lon2, lat2):

        lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

        newlon = lon2 - lon1
        newlat = lat2 - lat1
        
        haver_formula = np.sin(newlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(newlon/2.0)**2

        dist = 2 * np.arcsin(np.sqrt(haver_formula ))
        km = 6367 * dist #6367 for distance in KM for miles use 3958
        return km

    df['dist_km'] = haversine_vectorize(df['Longitude'],df['Latitude'],lon2,lat2)
    df=df.sort_values('dist_km')
    df['cost_RS']=np.ceil(df['dist_km']/3)*10
    print(df.loc[:3])
# example
hub_finder(data,28.669000,77.453800)