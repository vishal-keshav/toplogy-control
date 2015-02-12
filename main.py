# Author: Vishal Keshav
# Github: www.github.com/bulletcross/topology-control

import _generator as gen
import _utility as ut

"""This is main script used for different topology control algorithm analysis"""

def main():
    graph_constructor = gen.Connected(20,5,50,50)
    G = graph_constructor.generate_graph()
    ut.plot_graph(G)

if __name__ == '__main__':
    main()
