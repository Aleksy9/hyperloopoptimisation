
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
from Mapping import points,combined_population,distance_links,links, cities

plotting = False #True to see sensitivity plots, False to get NL network result

#Changing the following parameters:
#   - 2Ticket price
#   - 1price per tube
#   - 3price per vehicle
#   - max. #vehicles per tube
#   - 3max. #persons per vehicle
#   - 3Vehicle operation cost
#   - reduction of maintenance + operational cost

it_n = 35 #number of points calculated
year = 1
ratio = np.linspace(1,45,it_n)
ratio_decr = 1/ratio

ticket_price = distance_links * 0.5 * 10 ** (-6)
vehicl_ops_price = 3.695 * year
station_ops_price = 14.7799 * (0.5 + np.sqrt(1 + 8 * len(links)) / 2) * year
energy_price = 0.0000000115 * year
station_main_price = 0.71859 * (0.5 + np.sqrt(1 + 8 * len(links)) / 2) * year
tube_main_price = 0.056900 * distance_links * year
vehicl_main_price = 0.00054 * year
price_tube = distance_links * 25.61

pt_lst= it_n*[price_tube] #np.multiply.outer(ratio_decr,price_tube)                         #price per tube
pv_lst=it_n*[4.5]                                                                     #price per vehicle
max_nv_lst=it_n*[40]                                                                        #maximum number of vehicles per tube
max_np_lst= it_n*[438000] #ratio*[438000]                                                   #maximum number of passengers per vehicle
pr_lst = np.multiply.outer(ratio,ticket_price)                                          #ticket price
vehic_ops_lst = it_n*[vehicl_ops_price] #ratio_decr*[vehicl_ops_price]                      #vehicle operation cost
station_ops_lst = it_n*[station_ops_price] #ratio_decr*[station_ops_price]                  #station cost
energy_cost_lst = it_n*[energy_price] #ratio_decr*[energy_price]                            #energy cost per passenger
station_main_lst = it_n*[station_main_price] #ratio_decr*[station_main_price]               #station maintenance cost
tube_main_lst = it_n*[tube_main_price] #np.multiply.outer(ratio_decr, tube_main_price)       #tube maintenance cost
vehicles_main_lst = it_n*[vehicl_main_price] #ratio_decr*[vehicl_main_price]                 #vehicles maintenance

#Parameters to be collected:
#   - Objective function value / 100
#   - Number of links
#   - Number of vehicles
#   - Number of passengers / 100,000 transported
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

for n in range(it_n):
    pt = pt_lst[n]
    pv = pv_lst[n]
    max_nv = max_nv_lst[n]
    max_np = max_np_lst[n]
    # ticket price based on price per kilometer
    pr = pr_lst[n]

    # operational costs per year
    vehic_ops = vehic_ops_lst[n]
    station_ops = station_ops_lst[n]
    energy_cost = energy_cost_lst[n]  # (per 1 seat per km)
    # maintenance costs per year
    station_main = station_main_lst[n]
    tube_main = tube_main_lst[n]
    vehicles_main = vehicles_main_lst[n]  # per seat

    #---------------------------------------------------------------------------------#

    cwd = os.getcwd()

    # Keep track of start time to compute overall comptuational performance
    startTimeSetUp = time.time()
    # Initialize empty model
    model = Model()

    #-----------constant----------

    # city coordinates
    coord = points
    # maximum passengers per line per year
    p = [int(combined_population[i] * 0.47 * 2) for i in range(len(links))]
    # maximum number of tubes
    max_tubes = 1

    # cost of land/design and planning for the corridors is estimated to be 25% of the infrastructure price
    c = [pt[i] * 0.25 for i in range(len(links))]

    # setting up variables ======================================
    # node numbers
    numbers = links


    # create list of all indices that connect one node
    indices = np.array([])
    s = []
    for i in range(len(numbers)):

        for j in range(len(numbers)):

            s = [int(l) for l in re.findall(r'\d+', numbers[j])]

            for k in s:

                if k == i + 1:
                    indices = np.append(indices, int(j))


    # creating numbers flipped array
    def flip_numbers(array):
        numbers_flipped = []
        s = []
        v = [0, 0]
        l = ''
        for i in range(len(array)):
            s = [int(l) for l in re.findall(r'\d+', array[i])]

            l = "%s" % s[1] + "_%s" % s[0]
            numbers_flipped.append(l)
        return numbers_flipped


    # number of passengers per line

    pax = {}
    for i in range(0, len(numbers)):
        pax[i] = model.addVar(lb=0, ub=p[i], vtype=GRB.INTEGER, name="pax_%s" % (numbers[i]))

    # build a line yes/no

    x = {}
    for i in range(0, len(numbers)):
        x[i] = model.addVar(lb=0, vtype=GRB.BINARY, name="x_%s" % (numbers[i]))

    y = {}
    for i in range(0, len(numbers)):
        y[2 * i] = model.addVar(lb=0, vtype=GRB.BINARY, name="y_%s" % (numbers[i]))
        y[2 * i + 1] = model.addVar(lb=0, vtype=GRB.BINARY, name="y_%s" % (flip_numbers(numbers)[i]))

    # number of tubes between two points

    nt = {}
    for i in range(0, len(numbers)):
        nt[i] = model.addVar(lb=0, vtype=GRB.INTEGER, name="nt_%s" % (numbers[i]))

    # number of vehicles between two points

    nv = {}
    for i in range(0, len(numbers)):
        nv[i] = model.addVar(lb=0, vtype=GRB.INTEGER, name="nv_%s" % (numbers[i]))

    model.update()

    # setting up constraints =========================================
    thisLHS = LinExpr()

    # maximum amount of tubes per line constraint
    for i in range(0, len(numbers)):
        thisLHS = LinExpr()
        thisLHS += nt[i] - x[i] * max_tubes
        model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0, name="max_tubes_%s" % (numbers[i]))

    # maximum number of vehicles per line
    for i in range(0, len(numbers)):
        thisLHS = LinExpr()
        thisLHS += nv[i] - nt[i] * max_nv
        model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0, name="max_vehicles_%s" % (numbers[i]))

    # if a link is active, have at least 1 tube constructed
    for i in range(0, len(numbers)):
        thisLHS = LinExpr()
        thisLHS += nt[i] - x[i]
        model.addConstr(lhs=thisLHS, sense=GRB.GREATER_EQUAL, rhs=0, name="activate_tube_%s" % numbers[i])

    # if a tube is built, we require at least one vehicle to run in it
    for i in range(0, len(numbers)):
        thisLHS = LinExpr()
        thisLHS += nv[i] - x[i]
        model.addConstr(lhs=thisLHS, sense=GRB.GREATER_EQUAL, rhs=0, name="activate_vehicle_%s" % numbers[i])

    # maximum amount of passengers between two lines based on number of vehicles
    for i in range(0, len(numbers)):
        thisLHS = LinExpr()
        thisLHS += pax[i] - nv[i] * max_np
        model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0, name="max_passengers_vehicle%s" % (numbers[i]))

    # equal amount of passengers to demand between cities
    for i in range(0, len(numbers)):
        thisLHS = LinExpr()
        thisLHS += pax[i] - p[i]
        model.addConstr(lhs=thisLHS, sense=GRB.LESS_EQUAL, rhs=0, name="max_passengers_%s" % (numbers[i]))

    # 2 have n-1 links active
    thisLHS = LinExpr()
    for i in range(0, len(numbers)):
        thisLHS += x[i]
    model.addConstr(lhs=thisLHS, sense=GRB.EQUAL, rhs=(0.5 + np.sqrt(1 + 8 * len(numbers)) / 2 - 1),
                    name="min_amount_links")

    # -----new subtour elimination method-----
    # constraint 1
    for i in range(0, len(numbers)):
        thisLHS = LinExpr()
        thisLHS += x[i] - y[2 * i] - y[2 * i + 1]
        model.addConstr(lhs=thisLHS, sense=GRB.EQUAL, rhs=0, name="martin_method_first_constraint_%s" % (i + 1))

    # constraint 2
    # preprocessing
    y_numbers = []
    for i in range(len(numbers)):
        y_numbers.append(numbers[i])
        y_numbers.append(flip_numbers(numbers)[i])

    for i in range(0, len(numbers)):
        thisLHS = LinExpr()
        thisLHS += x[i]
        sx = [int(l) for l in re.findall(r'\d+', numbers[i])]
        for j in range(0, len(y_numbers)):
            sy = [int(l) for l in re.findall(r'\d+', y_numbers[j])]

            if sx[1] == sy[1] and sx[0] != sy[0]:
                thisLHS += y[j]

        model.addConstr(lhs=thisLHS, sense=GRB.EQUAL, rhs=1, name="martin_method_second_constraint_%s" % (i + 1))

    model.update()

    # Defining objective function

    obj = LinExpr()

    # objective function
    for i in range(0, len(numbers)):
        obj += pr[i] * pax[i] * year
        obj -= c[i] * nt[i]
        obj -= pt[i] * nt[i]
        obj -= (pv + vehic_ops) * nv[i]
        obj -= energy_cost * max_np * nv[i]
        obj -= tube_main[i] * nt[i]
        obj -= vehicles_main * 50 * nv[i]  # 50 is amount of seats in a vehicle
    obj -= station_ops
    obj -= station_main

    model.setObjective(obj, GRB.MAXIMIZE)
    # Updating the model
    model.update()
    # Writing the .lp file.
    model.write('model_formulation.lp')

    model.optimize()
    # Keep track of end time to compute overall computational performance
    endTime = time.time()

    # Saving our solution in the form [name of variable, value of variable]
    solution = [['Objective value', int(model.ObjVal)]]
    for v in model.getVars():
        solution.append([v.varName, v.x])



    # ----GETTING DATA AND PLOTTING OF RESULTS--------#


    data = get_data(solution)
    number_passengers_it = list()
    number_links_it = list()
    number_tubes_it = list()
    number_vehicles_it = list()
    for info in data:
        if info[0] == 'Objective value':
            obj_lst.append(info[1]/100) ##
        elif info[0][0] == 'p':
            number_passengers_it.append(info[1])
        elif info[0][0] == 'x':
            number_links_it.append(info[1])
        elif info[0][1] == 't':
            number_tubes_it.append(info[1])
        elif info[0][1] == 'v':
            number_vehicles_it.append(info[1])


    number_passengers_lst.append(sum(number_passengers_it)/100000) ##
    number_links_lst.append(sum(number_links_it))
    number_tubes_lst.append(sum(number_tubes_it))
    number_vehicles_lst.append(sum(number_vehicles_it))

    # ------ alternatve plotting ------------#
    # results visualisation
    # city coordinates

    if n == 0:
        # print('plotting')
        # print(model.ObjVal)
        # print(sum(number_passengers_it))
        # print(sum(number_vehicles_it))
        # print(solution)
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

#----------plotting---------------#
if plotting:
    plt.clf()
    plt.plot(ratio, obj_lst, label = 'Objective value/100')
    plt.plot(ratio, number_links_lst, label = 'Number of links')
    plt.plot(ratio, number_vehicles_lst,label = 'Number of vehicles')
    plt.plot(ratio, number_passengers_lst, label = 'Number of passengers/100,000')
    plt.plot(ratio, number_tubes_lst,label = 'Number of tubes')

    plt.legend(loc='lower right')
    plt.title('Change of parameters as a function of decreasing maintenance and operational cost for the stations, tubes and energy cost')
    plt.xlabel('Decrease ratio of maintenance and operational cost')
    plt.grid()
    plt.rcParams.update({'font.size': 17})
    plt.show()


