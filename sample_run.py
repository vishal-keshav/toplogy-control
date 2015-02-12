import random as rnd
import networkx as net
from matplotlib import pyplot as plt

def display_graph(G):
    #Creating Dictionary for positioning
    pos={}
    for n in G:
        pos[n]=(G.node[n]['x'],G.node[n]['y'])
    net.draw(G,pos)
    #print pos
    plt.show()

def generate_graph(nodes,radius,a,b):
    #Generating initial position
    G=net.Graph()
    node_list= range(2,nodes+1)
    rnd.shuffle(node_list)
    x_coord=rnd.randint(0,a)
    y_coord=rnd.randint(0,b)
    #print node_list
    G.add_node(1,x=x_coord,y=y_coord);
    #Now adding nodes such that graph remain connected
    for i in node_list:
        #pick any node from current graph
        random_node = rnd.choice(G.nodes())
        #Randomly place node in vicinity of random node
        random_angle = rnd.random()*math.pi*2
        random_radius = rnd.random()*radius*2
        random_x = G.node[random_node]['x']+random_radius*math.sin(random_angle)
        random_y = G.node[random_node]['y']+random_radius*math.cos(random_angle)
        G.add_node(i,x=random_x,y=random_y)
        G.add_edge(random_node,i)
        #place the new node in graph
        #G.add_node(i,x_coord=random_x,y_coord=random_y)
        #Connecting it to possible nodes in vicinity
        #print G.nodes()
        for j in G.node:
            if distance(G.node[j]['x'],G.node[j]['y'],random_x,random_y)<radius:
                G.add_edge(i,j)
    #print G.nodes()
    #print G.edges()
    #print G.node
    #print G[1]['x']
    return G

def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

G=generate_graph(100,100,300,300)
display_graph(G)
