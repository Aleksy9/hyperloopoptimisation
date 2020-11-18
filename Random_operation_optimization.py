# https://github.com/Aleksy9/hyperloopoptimisation.git
import random
import numpy as np

np.random.seed(101)



class Data_Generation():
    
    def __init__(self, nodes,  minimum = 1, maximum = 10, connected=True):
        self.nodes = nodes
        self.connected = connected
        self.minimum = minimum 
        self.maximum = maximum
        
    def create_nodes(self):
        pointsX = np.random.rand(self.nodes,1)*self.maximum
        pointsY = np.random.rand(self.nodes,1)*self.maximum
        
        dist = []
        connections = []
        
        for i, x in enumerate(pointsX):
            dist.append(np.sqrt((x-pointsX[i+1::])**2 + (pointsY[i]-pointsX[i+1::])**2 ))
            for j in range(len(pointsX[i+1::])):
                connections.append(f"{i+1}_{i+j+2}")
        
        return dist, connections, pointsX, pointsY
    
    def create_other_data(self):
        
        def Sum(nodes):
            number = 0
            for x in range(nodes):
                number += x
            return number
                
                
        amount_passengers_node = np.random.randint(self.minimum, self.maximum, Sum(self.nodes))*20
        Ticket_price_node =  np.random.randint(self.minimum, self.maximum, Sum(self.nodes))
        land_cost_node =  np.random.randint(self.minimum+1, self.maximum, Sum(self.nodes))
        amount_vehicles_tube =  np.random.randint(self.minimum+1, self.maximum, Sum(self.nodes))
        price_vehicle = np.random.randint(self.minimum+1,self.maximum)
        number_passengers_vehicle = np.random.randint(self.minimum+1,self.maximum)
        max_tubes_rand = np.random.randint(self.minimum+1, self.maximum, Sum(self.nodes))
        
        return amount_passengers_node, Ticket_price_node, land_cost_node, amount_vehicles_tube, price_vehicle, number_passengers_vehicle, max_tubes_rand
       
    


Nodes_tryout = Data_Generation(14, 1,10)

dist, connections, pointsX, pointsY = Nodes_tryout.create_nodes()
amount_passengers_node, Ticket_price_node, land_cost_node, amount_vehicles_tube, price_vehicle, number_passengers_vehicle, max_tubes_rand= Nodes_tryout.create_other_data()

points=np.ones((len(pointsX),2))
points[:,0]=pointsX[:,0]

points[:,1]=pointsY[:,0]


#f= open("LPsolve.Ip","w+")
#
#for i in range(nodes):
#     f.write()
#
#f.close()    

