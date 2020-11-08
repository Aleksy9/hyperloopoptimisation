
import numpy as np
import os
import pandas as pd
import time
from gurobipy import Model,GRB,LinExpr
import pickle
from copy import deepcopy

cwd = os.getcwd()

# Keep track of start time to compute overall comptuational performance
startTimeSetUp = time.time()
# Initialize empty model
model = Model()

#constant

#maximum passengers per line
p=np.array([5,10,15])

#cost of land
c=np.array([2,5,5])

#maximum number of tubes
max_tubes=np.array([2,2,2])

#ticket price
pr=np.array([2,2,5])

pt=1 #price per tube
pv=2 #price per vehicle
max_nv=1 #maximum number of vehicles per tube
max_np=5 #maximum number of passengers per vehicle


#setting up variables ======================================
#node numbers
numbers=["12","23","31"]

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



#setting up constraints
thisLHS=LinExpr()
#maximum amount of tubes per line constraint
for i in range(0,len(numbers)):
    thisLHS=LinExpr()
    thisLHS+= nt[i]-x[i]*max_tubes[i]
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
    model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0,name="max_passengers%s"%(numbers[i]))
    
model.update()
    


#Defining objective function

obj=LinExpr()

# Adding each crash cost and associated decision variable to the
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
model.write('model_formulation.lp')    

# Here the model is actually being optimized
model.optimize()
# Keep track of end time to compute overall comptuational performance 
endTime   = time.time()

# Saving our solution in the form [name of variable, value of variable]
solution = []
for v in model.getVars():
     solution.append([v.varName,v.x])
     
print(solution)







