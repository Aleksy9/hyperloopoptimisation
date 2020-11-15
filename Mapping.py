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
links=[]
distance=np.array([])
combined_population=np.array([])
pop=0
d=0
for i in range(len(lat)):
    
    for j in range(i+1,len(lat)):
        d= 2*np.pi/360 * R* np.arccos(np.cos(lat[i])*np.cos(lon[i])*np.cos(lat[j])*np.cos(lat[j])+np.cos(lat[i])*np.sin(lon[i])*np.cos(lat[j])*np.sin(lat[j])+np.sin(lat[i])*np.sin(lat[j]))
        pop=population[i]+population[j]
        distance=np.append(distance,d)
        links.append(f"{i+1}_{j+1}")
        combined_population=np.append(combined_population,pop)
        
    
    
  


print(combined_population)

plt.scatter(lon,lat)

for i in range(len(lat)):
    plt.text(lon[i]-0.25,lat[i]+0.05,label[i])

plt.show()


