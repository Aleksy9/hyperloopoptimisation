
import numpy as np
import os
import pandas as pd
import time
from gurobipy import Model,GRB,LinExpr
import pickle
from copy import deepcopy
import matplotlib.pyplot as plt
import re
from Random_operation_optimization import points, dist, connections,amount_passengers_node, Ticket_price_node, land_cost_node, amount_vehicles_tube, price_vehicle, number_passengers_vehicle, max_tubes_rand

plotting = True

#Changing the following parameters:
#   - price per tube
#   - price per vehicle
#   - max. #vehicles per tube
#   - max. #vehicles per vehicle
#   - Ticket price
#   - Vehicle operation cost
#   - reduction of maintenance + operational cost

pt_lst=[1,1,1,1,1,1]        #price per tube
pv_lst=[2,2,2,2,2,2]        #price per vehicle
max_nv_lst=[1,2,3,4,5,6]    #maximum number of vehicles per tube
max_np_lst=[5,5,5,5,5,5]    #maximum number of passengers per vehicle

#Parameters to be collected:
#   - Objective function value / 100
#   - Number of links
#   - Number of vehicles
#   - Number of passengers / 10
#   - Number of tubes

obj_lst = list()
number_links_lst = list()
number_vehicles_lst = list()
number_passengers_lst = list()
number_tubes_lst = list()

#--------function----------

def get_data(solution):
    data_result = list()
    data_result.append(solution[0])
    for data in solution:
        if int(data[1]) != 0 and data[0] != 'Objective value':
            data_result.append(data)
    return data_result


######-------------------MAIN LOOP-----------------------######

for i in range(len(pt_lst)):
    pt = pt_lst[i]
    pv = pv_lst[i]
    max_nv = max_nv_lst[i]
    max_np = max_np_lst[i]

    cwd = os.getcwd()

    # Keep track of start time to compute overall comptuational performance
    startTimeSetUp = time.time()
    model = Model()

    # constant

    # city coordinates
    coord = points

    # maximum passengers per line
    p = amount_passengers_node

    # cost of land
    c = land_cost_node

    # maximum number of tubes
    max_tubes = max_tubes_rand

    # ticket price
    pr = Ticket_price_node

    # setting up variables ======================================
    # node numbers
    numbers = connections

    # create list of all indices that connect one node
    indices = np.array([])
    s = []
    for i in range(len(numbers)):

        for j in range(len(numbers)):

            s = [int(l) for l in re.findall(r'\d+', numbers[j])]

            for k in s:

                if k == i + 1:
                    indices = np.append(indices, int(j))

    # number of passengers per line

    pax = {}
    for i in range(0, len(numbers)):
        pax[i] = model.addVar(lb=0, ub=p[i], vtype=GRB.INTEGER, name="pax_%s" % (numbers[i]))

    # build a line yes/no

    x = {}
    for i in range(0, len(numbers)):
        x[i] = model.addVar(lb=0, vtype=GRB.BINARY, name="x_%s" % (numbers[i]))

    # number of tubes between two points

    nt = {}
    for i in range(0, len(numbers)):
        nt[i] = model.addVar(lb=0, vtype=GRB.INTEGER, name="nt_%s" % (numbers[i]))

    # number of vehicles between two points

    nv = {}
    for i in range(0, len(numbers)):
        nv[i] = model.addVar(lb=0, vtype=GRB.INTEGER, name="nv_%s" % (numbers[i]))

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

    # Defining objective function

    obj = LinExpr()

    # objective function
    for i in range(0, len(numbers)):
        obj += pr[i] * pax[i]
        obj -= c[i] * x[i]
        obj -= pt * nt[i]
        obj -= pv * nv[i]

    # Important: here we are telling the solver we want to minimize the objective
    # function. Make sure you are selecting the right option!
    model.setObjective(obj, GRB.MAXIMIZE)
    # Updating the model
    model.update()
    # Writing the .lp file. Important for debugging
    model.write('model_formulation.lp')

    # Here the model is actually being optimized
    model.optimize()
    # Keep track of end time to compute overall comptuational performance
    endTime = time.time()

    obj = model.ObjVal
    # Saving our solution in the form [name of variable, value of variable]
    solutionver = [["Objective value", obj]]
    for v in model.getVars():
        solutionver.append([v.varName, v.x])


    # results visualisation
    # city coordinates

    #
    # plt.scatter(coord[:, 0], coord[:, 1])
    #
    # s = 0
    #
    # # Function of loop: finds active links then plots line between nodes of each active link
    # for i in range(0, len(numbers)):
    #     if solution[i + len(numbers)+1][1] >= 0.9:
    #         s = [int(j) for j in re.findall(r'\d+', solution[i + len(numbers)][0])]
    #
    #         plt.plot((coord[s[0] - 1, 0], coord[s[1] - 1, 0]), (coord[s[0] - 1, 1], coord[s[1] - 1, 1]), label=numbers[i])
    # plt.legend()
    # plt.show()

    # ----GETTING DATA AND PLOTTING OF RESULTS--------#


    data = get_data(solutionver)
    number_passengers_it = list()
    number_links_it = list()
    number_tubes_it = list()
    number_vehicles_it = list()
    for info in data:
        if info[0] == 'Objective value':
            obj_lst.append(info[1]/100)
        elif info[0][0] == 'p':
            number_passengers_it.append(info[1])
        elif info[0][0] == 'x':
            number_links_it.append(info[1])
        elif info[0][1] == 't':
            number_tubes_it.append(info[1])
        elif info[0][1] == 'v':
            number_vehicles_it.append(info[1])


    number_passengers_lst.append(sum(number_passengers_it)/10)
    number_links_lst.append(sum(number_links_it))
    number_tubes_lst.append(sum(number_tubes_it))
    number_vehicles_lst.append(sum(number_vehicles_it))

#----------plotting---------------#
if plotting:
    plt.plot(max_nv_lst, obj_lst, label = 'Objective value/100')
    plt.plot(max_nv_lst, number_links_lst, label = 'Number of links')
    plt.plot(max_nv_lst, number_vehicles_lst,label = 'Number of vehicles')
    plt.plot(max_nv_lst, number_passengers_lst, label = 'Number of passengers/10')
    plt.plot(max_nv_lst, number_tubes_lst,label = 'Number of tubes')

    plt.legend(loc='upper right')
    plt.title('Change of parameters as a function of number of maximum number of vehicles')
    plt.xlabel('Maximum number of vehicles')
    plt.show()
