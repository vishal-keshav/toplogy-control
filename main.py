# Author: Vishal Keshav
# Github: www.github.com/bulletcross/topology-control

import _generator as gen
import _utility as ut
import networkx as net

"""This is main script used for different topology control algorithm analysis"""

def main():
    #graph_constructor = gen.Connected(20,5,40,40)
    #G = graph_constructor.generate_graph()
    #ut.plot_graph(G)
    graph_constructor2 = gen.Connected(50,10,100,100)
    G2 = graph_constructor2.generate_graph()
    ut.plot_graph(G2)

    #G4 = G2.to_undirected()
    #print G4.edge
    
    print G2.number_of_edges()
    G3 = ut.relative_neighbor_topology_control(G2)
    print G3.number_of_edges()
    ut.plot_graph(G3)
    rho = ut.strech_factor(G3,G2)
    print rho
    
if __name__ == '__main__':
    main()
