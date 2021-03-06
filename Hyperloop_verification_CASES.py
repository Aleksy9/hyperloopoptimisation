
import numpy as np
import os
import pandas as pd
import time
from gurobipy import Model,GRB,LinExpr
import pickle
from copy import deepcopy
import matplotlib.pyplot as plt
import re

cwd = os.getcwd()

# Keep track of start time to compute overall comptuational performance
startTimeSetUp = time.time()
# Initialize empty model
model = Model()

#constant

#city coordinates
coord=np.array([[-1,-1],[-1,1],[1,1]])

#maximum passengers per line
p=np.array([5,15,10]) #link 1-2,1-3,2-3

#cost of land
c=np.array([7,45,100])

#maximum number of tubes
max_tubes=np.array([2,2,2])

#ticket price
pr=np.array([2,5,2])

pt=1 #price per tube
pv=2 #price per vehicle
max_nv=1 #maximum number of vehicles per tube
max_np=5 #maximum number of passengers per vehicle


#setting up variables ======================================
#node numbers
numbers=["1_2","1_3","2_3"]

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

# setting up constraints
thisLHS = LinExpr()
# maximum amount of tubes per line constraint
for i in range(0, len(numbers)):
    thisLHS = LinExpr()
    thisLHS += nt[i] - x[i] * max_tubes[i]
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0, name="max_tubes_%s" % (numbers[i]))

# force the number of tubes to be >= 1 when link is active
for i in range(0, len(numbers)):
    thisLHS = LinExpr()
    thisLHS += nt[i] - x[i]
    model.addConstr(lhs=thisLHS, sense=GRB.GREATER_EQUAL, rhs=0, name="min_tubes_%s" % (numbers[i]))

# maximum number of vehicles per line

for i in range(0, len(numbers)):
    thisLHS = LinExpr()
    thisLHS += nv[i] - nt[i] * max_nv
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0, name="max_vehicles_%s" % (numbers[i]))

# maximum amount of passengers between two lines based on number of vehicles

for i in range(0, len(numbers)):
    thisLHS = LinExpr()
    thisLHS += pax[i] - nv[i] * max_np
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0, name="max_passengers_%s" % (numbers[i]))

print(int(0.5 + np.sqrt(1 + 8 * len(numbers)) / 2))

# Have all nodes connected at least once (requires 2 constraints to avoid subtours)
# 1 have each node have at least one link to it
print(len(numbers))
for i in range(0, int(0.5 + np.sqrt(1 + 8 * len(numbers)) / 2)):
    thisLHS = LinExpr()
    for j in range(0, int(0.5 + np.sqrt(1 + 8 * len(numbers)) / 2) - 1):
        thisLHS += -x[indices[i * (int(0.5 + np.sqrt(1 + 8 * len(numbers)) / 2) - 1) + j]]

    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=-1, name="node_connected_%s" % (i + 1))

# 2 have at least n-1 links active
thisLHS = LinExpr()
for i in range(0, len(numbers)):
    thisLHS += x[i]
model.addConstr(lhs=thisLHS, sense=GRB.EQUAL, rhs=(0.5 + np.sqrt(1 + 8 * len(numbers)) / 2 - 1),
                name="min_amount_links")

model.update()



#Defining objective function

obj=LinExpr()


# objective function
for i in range(0,len(numbers)):
    obj+=pr[i]*pax[i]
    obj-=c[i]*x[i]
    obj-=pt*nt[i]
    obj-=pv*nv[i]

# Important: here we are telling the solver we want to minimize the objective
# function. Make sure you are selecting the right option!    
model.setObjective(obj,GRB.MAXIMIZE)
# Updating the model
model.update()
# Writing the .lp file. Important for debugging
model.write('model_formulation2.lp')

# Here the model is actually being optimized
model.optimize()
# Keep track of end time to compute overall comptuational performance 
endTime = time.time()

#objective value result
obj = model.ObjVal

# Saving our solution in the form [name of variable, value of variable]
solution2 = [["Objective value", obj]]
for v in model.getVars():
     solution2.append([v.varName,v.x])




#results visualisation
#city coordinates

plt.scatter(coord[:,0],coord[:,1])

s=0

#Function of loop: finds active links then plots line between nodes of each active link
for i in range(0,len(numbers)):
    if solution2[i+len(numbers)+1][1]>=0.9:
        
        s=[int(j) for j in re.findall(r'\d+', solution2[i+len(numbers)][0])]
        
        plt.plot((coord[s[0]-1,0],coord[s[1]-1,0]),(coord[s[0]-1,1],coord[s[1]-1,1]),label=numbers[i])
plt.legend()
plt.show()

#----GETTING DATA AND PLOTTING OF RESULTS--------#

def get_data(solution):
    data_result = list()
    data_result.append(solution[0])
    for data in solution:
        if int(data[1]) != 0:
            data_result.append(data)
    return data_result

data = get_data(solution2)
print(data)





