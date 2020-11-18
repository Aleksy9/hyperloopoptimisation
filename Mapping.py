# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:42:19 2020

@author: AlexisPC
"""

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import matplotlib.image as mpimg
from math import cos, asin, sqrt, pi

def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a)) #2*R*asin...

cities = pd.read_csv('nl.csv')

#constants
R=6371 #earth radius in km

# Extract the data we're interested in
lat = cities['lat'].values
lon = cities['lng'].values
population = cities['population'].values
label=cities['city'].values


img = mpimg.imread('map_nl_cropped.jpg')


points=np.ones((len(lat),2))
points[:,0]=lon

points[:,1]=lat


#making the required arrays
#we need to convert lat and long to radians

links=[]
distance_links=np.array([])
combined_population=np.array([])
pop=0
d=0
for i in range(len(lat)):
    
    for j in range(i+1,len(lat)):
        d=  distance(lat[i],lon[i],lat[j],lon[j])
        pop=population[i]+population[j]
        
        
        distance_links=np.append(distance_links,d)
        links.append(f"{i+1}_{j+1}")
        combined_population=np.append(combined_population,pop)
        
    
    
  


if __name__ == '__main__':
    print(distance_links)

plt.scatter(lon,lat)

for i in range(len(lat)):
    plt.text(lon[i]-0.25,lat[i]+0.05,label[i])

plt.show()


