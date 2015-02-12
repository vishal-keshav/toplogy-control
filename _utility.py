# Author:Vishal Keshav, Email:bulletcross@gmail.com
# Libraries and Modules has been used under Open Source Agreement
# Please confirm before distribution

"""This file contains utility functions including following topology control algorithms
    1. Cone based
    2. Relative Neighbouring
    3. Delauncy triangulation

    Utility function includes computaions of strech factor which in turn uses
    Floyed Warshall All pair shortest path Algorithm"""
import math
import networkx as net
from matplotlib import pyplot as plt

def plot_graph(Graph):
    """Uses matplotlib funtionality to plot graph"""
    #Creating Dictionary for positioning
    pos={}
    for n in Graph:
        pos[n]=(Graph.node[n]['x'],Graph.node[n]['y'])
    net.draw(Graph,pos)
    # TODO (bulletcross@gmail.com):Make Graph more apealing
    plt.show()

def distance(x1,y1,x2,y2):
    """Gives Euclidean Distances"""
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def minimum(a,b):
    """Gives minumum of two"""
    if a<b:
        return a
    else:
        return b


def strech_factor(Graph1,Graph2):
    """ Strech factor is the maximum ratio minimum weight path over Graph1/Graph2
        taken over all possible pair of vertices"""
    Matrix1 = floyd(Graph1);
    Matrix2 = floyd(Graph2);
    nodes=len(Graph.node)
    #Rho contains small value initially
    rho = 0
    for i in range(0,nodes):
        for j in range(0,nodes):
            if i!=j and rho<Matrix1[i][j]/Matrix2[i][j]:
                rho = Matrix1[i][j]/Matrix2[i][j]

def floyd(Graph):
    """This solves All pair shortest path length using basc algorthm"""
    nodes=len(Graph.node)
    INF = float("inf")
    #Initialisation of path weight matrix
    M=[[INF for i in range(nodes)] for j in range(nodes)]
    for i in range(1,nodes+1):
        M[i][i]=0
    for e in Graph.edges_iter():
        M[e[0]][e[1]]=M[e[1]][e[0]] = distance(Graph.node[e[0]]['x'],Graph.node[e[0]]['y'],Graph.node[e[1]]['x'],Graph.node[e[1]]['y'])
        
    #Main algorithm
    Range = range(0,nodes)
    for k in Range:
        for i in Range:
            for j in Range:
                M[i][j] = minimum(M[i][j],M[i][k]+M[k][j])
    return M

"""Topology control algorithm implementation"""
#TODO (bulletcross@gmail.com): Implement the algorithm and check strech factor

def cone_based_topology_control(Graph):
    pass

def relative_neighbor_topology_control(Graph):
    pass

def delauncy_triangulation_topology_control(Graph):
    pass
