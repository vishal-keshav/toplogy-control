# Author:Vishal Keshav, Email:bulletcross@gmail.com
# Libraries and Modules has been used under Open Source Agreement

import random as rnd
import networkx as net
import _utility as ut
import math


class GraphGenerator(object):
    """This is an interface that provides uniformity for creation of different
        graph with attributes

        Attributes:
            number of nodes
            maximum radius of communication
            a and b denotes area in which graph has to be laid"""
    
    def __init__(self, nodes, radius, a, b):
        self.nodes=nodes
        self.radius=radius
        self.a=a
        self.b=b

    def generate_graph(self):
        pass

class Connected(GraphGenerator):
    """This class inherits from Graph Generator and overrids the generate_graph
        functionality"""
        
    def generate_graph(self):
        #Generating initial position
        G=net.Graph()
        node_list= range(2,self.nodes+1)
        rnd.shuffle(node_list)
        x_coord=rnd.randint(0,self.a)
        y_coord=rnd.randint(0,self.b)
        G.add_node(1,x=x_coord,y=y_coord);

        #Now adding nodes such that graph remain connected
        for i in node_list:
            #pick any node from current graph
            random_node = rnd.choice(G.nodes())

            #Randomly place node in vicinity of random node
            random_angle = rnd.random()*math.pi*2
            random_radius = rnd.random()*self.radius*2
            random_x = G.node[random_node]['x']+random_radius*math.sin(random_angle)
            random_y = G.node[random_node]['y']+random_radius*math.cos(random_angle)

            G.add_node(i,x=random_x,y=random_y)
            G.add_edge(random_node,i)

            """Randomly Generated points try to associate with every node which are
                reachable from its transmission range"""
            
            for j in G.node:
                if ut.distance(G.node[j]['x'],G.node[j]['y'],random_x,random_y)<self.radius:
                    G.add_edge(i,j)
        #TODO(bulletcross@gmail.com):Fix this function
        #Adding edge weight to each edge in the graph
        #for e in G.edges_iter():
        #    ut.add_attribute_to_edge(G,e[0],e[1],'w',ut.distance(G.node[e[0]]['x'],G.node[e[0]]['y'],G.node[e[1]]['x'],G.node[e[1]]['y']))
        return G

class Random(GraphGenerator):
    """This class inherits from Graph generator and provides the funtionality of
        creating a random graph"""
        
    def generate_graph(self):
        pass
