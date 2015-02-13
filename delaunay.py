#Author: Vishal Keshav, Email:bulletcross@gmail.com
#Copyright notice: this is an improvement of version provided by Yury V. Rayabov(riabovvv@gmail.com)
#Verify authors before distribution

import networkx as nx
import scipy.spatial
 
def createTINgraph(Graph_input):
  """ This function takes Graph as an input, extracts position coordinates and Calculate Delaunay triangulation
        to give another Graph with starting vertex as zero"""
  point_graph = []
  for n in Graph_input.nodes_iter():
      point_graph.append([Graph_input.node[n]['x'],Graph_input.node[n]['y']])
                         
  TIN = scipy.spatial.Delaunay(point_graph)
  edges = set()
  # for each Delaunay triangle
  for n in xrange(TIN.nsimplex):
      # for each edge of the triangle
      # sort the vertices
      # (sorting avoids duplicated edges being added to the set)
      # and add to the edges set
      edge = sorted([TIN.vertices[n,0], TIN.vertices[n,1]])
      edges.add((edge[0], edge[1]))
      edge = sorted([TIN.vertices[n,0], TIN.vertices[n,2]])
      edges.add((edge[0], edge[1]))
      edge = sorted([TIN.vertices[n,1], TIN.vertices[n,2]])
      edges.add((edge[0], edge[1]))

  # make a graph based on the Delaunay triangulation edges
  graph = nx.Graph(list(edges))
  i=0
  for n in point_graph:
    graph.node[i]['x'] = n[0]
    graph.node[i]['y'] = n[1]
    i=i+1
  return graph
