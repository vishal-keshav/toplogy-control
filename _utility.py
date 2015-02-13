# Author:Vishal Keshav, Email:bulletcross@gmail.com
# Libraries and Modules has been used under Open Source Agreement
# Please confirm before distribution

"""This file contains utility functions including following topology control algorithms
    1. Cone based
    2. Relative Neighbouring
    3. Delaunay triangulation

    Utility function includes computaions of strech factor which in turn uses
    Floyed Warshall All pair shortest path Algorithm"""
import math
import networkx as net
import delaunay as dl
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

def maximum(a,b):
    """Gives maximum of two"""
    if a<b:
        return b
    else:
        return a

#TODO(bulletcross@gmail.com): Disable hardcoding with variable alpha
def find_block(angle):
    """This is used by cone based topology control algorithm"""
    if angle>=(-1)*math.pi and angle < (-2.0/3.0)*math.pi:
        return 0
    elif angle>=(-2.0/3.0)*math.pi and angle < (-1.0/3.0)*math.pi:
        return 1
    elif angle>=(-1.0/3.0)*math.pi and angle < (0)*math.pi:
        return 2
    elif angle>=(0)*math.pi and angle < (1.0/3.0)*math.pi:
        return 3
    elif angle>=(1.0/3.0)*math.pi and angle < (2.0/3.0)*math.pi:
        return 4
    elif angle>=(2.0/3.0)*math.pi and angle < (1)*math.pi:
        return 5
    else:
        return 0


def strech_factor(Graph1,Graph2):
    """ Strech factor is the maximum ratio minimum weight path over Graph1/Graph2
        taken over all possible pair of vertices"""
    Matrix1 = floyd(Graph1);
    Matrix2 = floyd(Graph2);
    nodes=len(Graph1.node)
    #Rho contains small value initially
    rho = 0
    for i in range(0,nodes):
        for j in range(0,nodes):
            if i!=j and rho < Matrix1[i][j]/Matrix2[i][j]:
                rho = Matrix1[i][j]/Matrix2[i][j]
    return rho

def floyd(Graph):
    """This solves All pair shortest path length using basc algorthm"""
    nodes=len(Graph.node)
    INF = float("inf")
    #Initialisation of path weight matrix
    M=[[INF for i in range(nodes)] for j in range(nodes)]
    for i in range(0,nodes):
        M[i][i]=0
    for e in Graph.edges_iter():
        M[e[0]-1][e[1]-1]= M[e[1]-1][e[0]-1] = distance(Graph.node[e[0]]['x'],Graph.node[e[0]]['y'],Graph.node[e[1]]['x'],Graph.node[e[1]]['y'])
    #Main algorithm
    Range = range(0,nodes)
    for k in Range:
        for i in Range:
            for j in Range:
                M[i][j] = minimum(M[i][j],M[i][k]+M[k][j])
    return M

#Add_attribute function is a contribution from Stefano C.
def add_attribute_to_edge(H,id_node_source,id_node_target,new_attr,value_attr):
    keydict =H[id_node_source][id_node_target]
    key=len(keydict)
    for k in keydict:
        if 'type' not in H.edge[id_source][id_target][k]:
            H.add_edge(id_node_source,id_node_target,key=k, new_attr= value_attr)

"""Topology control algorithm implementation"""

def cone_based_topology_control(Graph_input):
    """The Algorithm works as follow: it scans each nodes one after another. For each node,its neighbours are considered
        and area is diveded into six parts(alpha=pi/3). Nodes which are reachable with least power in each cone are
        connected under the constraint graph remains connected."""
    Graph = Graph_input.copy()
    verified_edges=[]
    for nd in Graph.nodes_iter():
        block = [0 for i in range(6)]
        node_neighbors = Graph.neighbors(nd)
        for n in node_neighbors:
            if nd!=n:
                angle = math.asin((Graph.node[n]['y']-Graph.node[nd]['y'])/distance(Graph.node[n]['x'],Graph.node[n]['y'],Graph.node[nd]['x'],Graph.node[nd]['y']))
                block_index = find_block(angle)
                if ((nd,n) in verified_edges) or ((n,nd) in verified_edges):
                    block[block_index]=n
                elif block[block_index]==0:
                    block[block_index]=n
                elif ((nd,block[block_index]) in verified_edges) or ((block[block_index],nd) in verified_edges):
                    pass
                else:
                    d_old = distance(Graph.node[nd]['x'],Graph.node[nd]['y'],Graph.node[block[block_index]]['x'],Graph.node[block[block_index]]['y'])
                    d_new = distance(Graph.node[nd]['x'],Graph.node[nd]['y'],Graph.node[n]['x'],Graph.node[n]['y'])
                    if d_old < d_new:
                        Graph.remove_edge(nd,n)
                        if not net.is_connected(Graph):
                            Graph.add_edge(nd,n)
                    else:
                        Graph.remove_edge(nd,block[block_index])
                        if not net.is_connected(Graph):
                            Graph.add_edge(nd,block[block_index])
                        else:
                            block[block_index] = n
        for nds in block:
            if (nd,nds) not in verified_edges:
                verified_edges.append((nd,nds))
            if (nds,nd) not in verified_edges:
                verified_edges.append((nds,nd))
    return Graph
    

def relative_neighbor_topology_control(Graph_input):
    """This algorithm utilises distance functionality to eliminate relative nodes. A scan through each edges is done and common neighbor
        is found, conditioned is applied and if it satisfies, edge is added to removal list(dynamic deletion is not possible with iterators)"""
    Graph = Graph_input.copy()
    removal_list=[]
    for e in Graph.edges_iter():
        node1=e[0]
        node2=e[1]
        node1_neighbors = Graph.neighbors(node1)
        node2_neighbors = Graph.neighbors(node2)
        #a node is considered connected to itself
        if node1!=node2:
            for n in node1_neighbors:
                #TODO(bulletcross@gmail.com):Use add_attribute funtion
                d1=distance(Graph.node[node1]['x'],Graph.node[node1]['y'],Graph.node[n]['x'],Graph.node[n]['y'])
                d2=distance(Graph.node[n]['x'],Graph.node[n]['y'],Graph.node[node2]['x'],Graph.node[node2]['y'])
                d12=distance(Graph.node[node1]['x'],Graph.node[node1]['y'],Graph.node[node2]['x'],Graph.node[node2]['y'])
                toggle = False
                if (n in node2_neighbors) and (maximum(d1,d2)<d12) and ((node1,n) not in removal_list) and ((node2,n) not in removal_list) and ((n,node1) not in removal_list) and ((n,node2) not in removal_list):
                    #Graph.remove_edge(node1,node2)
                    toggle = True
                    break
            if toggle:
                removal_list.append(e)
    for e in removal_list:
        Graph.remove_edge(*e)        
    return Graph

def delauncy_triangulation_topology_control(Graph_input):
    """This uses the inbulit library to for Delauny triangulation out of the node
        given in the Graph_input. Gelaunay graph along with Graph_input is compared
        to find the possibility of existance of an edge in original graph such that
        Graph remains connected"""
    Graph = Graph_input.copy()
    DGraph = dl.createTINgraph(Graph)
    #Incrementing node label by one
    mapping = {}
    for i in range(len(DGraph.node)):
        mapping[i]=i+1
    DGraph=net.relabel_nodes(DGraph,mapping)
    #Removing edges from original graph which are not the part of delaunay triangulation
    for e in Graph_input.edges_iter():
        if e not in DGraph.edge:
            Graph.remove_edge(*e)
            if not net.is_connected(Graph):
                Graph.add_edge(*e)
    return Graph
