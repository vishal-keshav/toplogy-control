# Author: Vishal Keshav
# Github: www.github.com/bulletcross/topology-control

import _generator as gen
import _utility as ut
import networkx as net

"""This is main script used for different topology control algorithm analysis"""

def main():

    #Generating a random graph based on input
    graph_constructor = gen.Connected(50,10,100,100)
    Graph_connected = graph_constructor.generate_graph()
    #Saving the generated graph in a file named main_graph
    ut.plot_graph(Graph_connected,"main_graph")

    print "-------Output for Relative neighbor topology control algorithm-------"
    print "Edges in original graph - " + str(Graph_connected.number_of_edges())
    Graph_RNG = ut.relative_neighbor_topology_control(Graph_connected)
    print "Egdes after RNG Algorithm - " + str(Graph_RNG.number_of_edges())
    ut.plot_graph(Graph_RNG,"RNG")
    print "Strech factor - " + str(ut.strech_factor(Graph_RNG,Graph_connected))
    print "Graph has been generated in the file named RNG.png"

    print "-------Output for Cone based topology control algorithm-------"
    print "Edges in original graph - " + str(Graph_connected.number_of_edges())
    Graph_cone = ut.cone_based_topology_control(Graph_connected)
    print "Egdes after Cone based Algorithm - " + str(Graph_cone.number_of_edges())
    ut.plot_graph(Graph_cone,"Cone")
    print "Strech factor - " + str(ut.strech_factor(Graph_cone,Graph_connected))
    print "Graph has been generated in the file named Cone.png"

    print "-------Output for Delaunay triangulation topology control algorithm-------"
    print "Edges in original graph - " + str(Graph_connected.number_of_edges())
    Graph_delaunay = ut.delaunay_triangulation_topology_control(Graph_connected)
    print "Egdes after Delaunay Algorithm - " + str(Graph_delaunay.number_of_edges())
    ut.plot_graph(Graph_delaunay,"Delaunay")
    print "Strech factor - " + str(ut.strech_factor(Graph_delaunay,Graph_connected))
    print "Graph has been generated in the file named Delaunay.png"
    
if __name__ == '__main__':
    main()
