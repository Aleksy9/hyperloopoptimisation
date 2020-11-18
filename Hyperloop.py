
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
from Mapping import points,combined_population,distance_links,links


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
max_tubes=2

#ticket price based on price per kilometer

pr=distance_links*0.5*10**(-6)

pt=distance_links*25.61 #price of construction of tube based on price (million CHF) per kilometre (distance between links times the cost per kilometre assuming we dont tunnel)
pv=4.500000 #price per vehicle (in million of CHF)
max_nv=40 #maximum number of vehicles per tube (source: hyperloop commercial feasibility analysis)
max_np=438000 #amount of passengers a vehicle can transport per year assuming 1 trip per hour

#cost of land/deign and planning for the corridors is estimated to be 25% of the infrastructure price
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

    

#number of passengers per line

pax={}
for i in range(0,len(numbers)):
    pax[i]=model.addVar(lb=0,ub=p[i],vtype=GRB.INTEGER,name="pax_%s"%(numbers[i]))


#build a line yes/no

x={}
for i in range(0,len(numbers)):
    x[i]=model.addVar(lb=0,vtype=GRB.BINARY,name="x_%s"%(numbers[i]))
    
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
 
#Have all nodes connected at least once (requires 2 constraints to avoid subtours)
#1 have each node have at least one link to it

for i in range(0,int(0.5+np.sqrt(1 + 8*len(numbers))/2)):
    thisLHS=LinExpr()
    for j in range(0,int(0.5+np.sqrt(1 + 8*len(numbers))/2)-1):
        
        thisLHS+= -x[indices[i*(int(0.5+np.sqrt(1 + 8*len(numbers))/2)-1)+j]]
    
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=-1,name="node_connected_%s"%(i+1))

#2 have at least n-1 links active 
thisLHS=LinExpr()
for i in range(0,len(numbers)):
    
    thisLHS+= x[i]
model.addConstr(lhs=thisLHS, sense=GRB.GREATER_EQUAL, rhs=(0.5+np.sqrt(1 + 8*len(numbers))/2-1),name="min_amount_links")

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
    obj+=pr[i]*pax[i]
    obj-=c[i]*x[i]
    obj-=pt[i]*nt[i]
    obj-=pv*nv[i]


    
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



plt.scatter(coord[:,0],coord[:,1])

s=0

#Function of loop: finds active links then plots line between nodes of each active link
for i in range(0,len(numbers)):
    if solution[i+len(numbers)][1]>=0.9:
        
        s=[int(j) for j in re.findall(r'\d+', solution[i+len(numbers)][0])]
        
        plt.plot((coord[s[0]-1,0],coord[s[1]-1,0]),(coord[s[0]-1,1],coord[s[1]-1,1]),label=numbers[i])
plt.legend()
plt.show()


#additional calculations from results

#revenue per year of operation
revenue=0
for i in range(0,len(numbers)):
    revenue+= solution[i][1]*pr[i]
    
print(revenue)




