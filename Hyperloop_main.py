
import numpy as np
import os
import pandas as pd
import time
from gurobipy import Model,GRB,LinExpr
import pickle
from copy import deepcopy
import matplotlib.pyplot as plt
import re
from Random_operation_optimization import dist, connections,amount_passengers_node, Ticket_price_node, land_cost_node, amount_vehicles_tube, price_vehicle, number_passengers_vehicle, max_tubes_rand
from Mapping import points,combined_population,distance_links,links, cities


cwd = os.getcwd()

# Keep track of start time to compute overall comptuational performance
startTimeSetUp = time.time()
# Initialize empty model
model = Model()

#constant

#city coordinates
coord=points

#maximum passengers per line per year
p=[int(combined_population[i]*0.47*2) for i in range(len(links))]



#maximum number of tubes
max_tubes=1

#ticket price based on price per kilometer

pr=distance_links*0.5*10**(-6)

#years of operation
year=1
ratio=1
#operational costs per year
vehic_ops=3.695*year*ratio
station_ops=14.7799*(0.5+np.sqrt(1 + 8*len(links))/2)*year*ratio
energy_cost=0.0000000115*year*ratio#(per 1 seat per km)

#maintenance costs per year
station_main=0.71859*(0.5+np.sqrt(1 + 8*len(links))/2)*year*ratio
tube_main=0.056900*distance_links*year*ratio
vehicles_main=0.00054*year*ratio #per seat

#fixed costs
pt=distance_links*25.61 #price of construction of tube based on price (million CHF) per kilometre (distance between links times the cost per kilometre assuming we dont tunnel)
pv=4.500000 #price per vehicle (in million of CHF)
max_nv=40 #maximum number of vehicles per tube (source: hyperloop commercial feasibility analysis)
max_np=438000 #amount of passengers a vehicle can transport per year assuming 1 trip per hour

#cost of land/design and planning for the corridors is estimated to be 25% of the infrastructure price
c=[pt[i]*0.25 for i in range(len(links))]

#setting up variables ======================================
#node numbers
numbers=links

#create list of all indices that connect one node
indices=np.array([])
s=[]
for i in range(len(numbers)):
    
    
    for j in range(len(numbers)):
        
        s= [int(l) for l in re.findall(r'\d+', numbers[j])]
    
        for k in s:
    
            if k==i+1:
                indices=np.append(indices,int(j))

#creating numbers flipped array
def flip_numbers(array):
    numbers_flipped=[]
    s=[]
    v=[0,0]
    l=''
    for i in range(len(array)):
        s= [int(l) for l in re.findall(r'\d+', array[i])]
        
        l="%s"%s[1]+"_%s"%s[0]
        numbers_flipped.append(l)
    return numbers_flipped
#number of passengers per line

pax={}
for i in range(0,len(numbers)):
    pax[i]=model.addVar(lb=0,ub=p[i],vtype=GRB.INTEGER,name="pax_%s"%(numbers[i]))


#build a line yes/no

x={}
for i in range(0,len(numbers)):
    x[i]=model.addVar(lb=0,vtype=GRB.BINARY,name="x_%s"%(numbers[i]))
    
y={}
for i in range(0,len(numbers)):
    y[2*i]=model.addVar(lb=0,vtype=GRB.BINARY,name="y_%s"%(numbers[i]))
    y[2*i+1]=model.addVar(lb=0,vtype=GRB.BINARY,name="y_%s"%(flip_numbers(numbers)[i]))
    
#number of tubes between two points

nt={}
for i in range(0,len(numbers)):
    nt[i]=model.addVar(lb=0,vtype=GRB.INTEGER,name="nt_%s"%(numbers[i]))

#number of vehicles between two points

nv={}
for i in range(0,len(numbers)):
    nv[i]=model.addVar(lb=0,vtype=GRB.INTEGER,name="nv_%s"%(numbers[i]))

     
model.update()



#setting up constraints =========================================
thisLHS=LinExpr()
#maximum amount of tubes per line constraint

for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+= nt[i]-x[i]*max_tubes
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0,name="max_tubes_%s"%(numbers[i]))

    
#maximum number of vehicles per line

for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+= nv[i]-nt[i]*max_nv
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0,name="max_vehicles_%s"%(numbers[i]))
 
#maximum amount of passengers between two lines based on number of vehicles

for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+= pax[i]-nv[i]*max_np
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0,name="max_passengers_vehicle%s"%(numbers[i]))
    
#equal amount of passengers to demand between cities
for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+= pax[i]-p[i]
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0,name="max_passengers_%s"%(numbers[i]))
 



#2 have n-1 links active 
thisLHS=LinExpr()
for i in range(0,len(numbers)):
    
    thisLHS+= x[i]
model.addConstr(lhs=thisLHS, sense=GRB.EQUAL, rhs=(0.5+np.sqrt(1 + 8*len(numbers))/2-1),name="min_amount_links")

#new subtour elimination method
#constraint 1
for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+=x[i]-y[2*i]-y[2*i+1]
    model.addConstr(lhs=thisLHS, sense=GRB.EQUAL, rhs=0,name="martin_method_first_constraint_%s"%(i+1))
    

#constraint 2
#preprocessing
y_numbers=[]
for i in range(len(numbers)):
    y_numbers.append(numbers[i])
    y_numbers.append(flip_numbers(numbers)[i])


for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+=x[i]
    sx=[int(l) for l in re.findall(r'\d+', numbers[i])]
    for j in range(0,len(y_numbers)):
        sy= [int(l) for l in re.findall(r'\d+', y_numbers[j])]
        
        if sx[1]==sy[1] and sx[0]!=sy[0]:
            thisLHS+=y[j]
    
    model.addConstr(lhs=thisLHS, sense=GRB.EQUAL, rhs=1,name="martin_method_second_constraint_%s"%(i+1))
        






#if a link is active, have at least 1 tube constructed

for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+= nt[i]-x[i]
    model.addConstr(lhs=thisLHS, sense=GRB.GREATER_EQUAL, rhs=0,name="activate_tube_%s"%numbers[i])

#if a tube is built, we require at least one vehicle to run in it

for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+= nv[i]-nt[i]
    model.addConstr(lhs=thisLHS, sense=GRB.GREATER_EQUAL, rhs=0,name="activate_vehicle_%s"%numbers[i])
model.update()
    





#Defining objective function

obj=LinExpr()


# objective function
for i in range(0,len(numbers)):
    obj+=pr[i]*pax[i]*year
    obj-=c[i]*nt[i]
    obj-=pt[i]*nt[i]
    obj-=(pv+vehic_ops)*nv[i]
    obj-=energy_cost*max_np*nv[i]
    obj-=tube_main[i]*nt[i]
    obj-=vehicles_main*max_np*nv[i]
obj-=station_ops
obj-=station_main
    
model.setObjective(obj,GRB.MAXIMIZE)
# Updating the model
model.update()
# Writing the .lp file.
model.write('model_formulation.lp')    


model.optimize()
# Keep track of end time to compute overall comptuational performance 
endTime   = time.time()

# Saving our solution in the form [name of variable, value of variable]
solution = []
for v in model.getVars():
     solution.append([v.varName,v.x])



#results visualisation
#city coordinates
img = plt.imread(r'nl_map.gif')
fig, ax = plt.subplots()

# Function of loop: finds active links then plots line between nodes of each active link
for i in range(0, len(numbers)):
    if solution[i + 4 * len(numbers)][1] >= 0.9:
        s = [int(j) for j in re.findall(r'\d+', solution[i + 4 * len(numbers)][0])]

        ax.plot((coord[s[0] - 1, 0], coord[s[1] - 1, 0]), (coord[s[0] - 1, 1], coord[s[1] - 1, 1]),
                label=numbers[i - 1])

# city coordinates
label = cities['city'].values
lon = coord[:, 0]
lat = coord[:, 1]
ax.scatter(lon, lat)
for i in range(len(lat)):
    ax.text(lon[i] - 0.25, lat[i] + 0.05, label[i])
ax.imshow(img, extent=[3.4, 7, 50.78, 53.5])
ax.legend()
ax.set_xlabel('longitude [°]')
ax.set_ylabel('lattitude [°]')
ax.set_title('Network for cities in The Netherlands')
ax.plot()



#additional calculations from results

#revenue per year of operation
revenue=0
for i in range(0,len(numbers)):
    revenue+= solution[i][1]*pr[i]*year

cost= 0
for i in range(0,len(numbers)):
    cost-=(vehic_ops)*solution[5*len(numbers)+i][1]+energy_cost*max_np*solution[5*len(numbers)+i][1]+tube_main[i]*solution[4*len(numbers)+i][1]
    cost-=vehicles_main*max_np*solution[5*len(numbers)+i][1]

cost-=station_ops
cost-=station_main
profit=revenue+cost
print(revenue,cost,profit)
