#!/usr/bin/python
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

'''
For the program to work, install the following software:

sudo apt-get install python3-tk 
sudo pip3 install networkx
sudo pip3 install matplotlib

Or with O.S. specific information and run as a Python3 file.
example: python3 prim.py city-pairs.txt
'''

# display_graph originally written by https://github.com/cteters, then modified by me
def display_graph(matrix):
    # create a graph to image
    G = nx.Graph()



    # fill the graph to be imaged with the matrix used
    for row in matrix:
        G.add_edge(nod_list[row[0]], nod_list[row[1]], weight=int(row[2]))

    edge = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G, k=40)  # positions for all nodes

    # weights
    weight = dict(map(lambda x: ((x[0], x[1]), str(x[2]['weight'])), G.edges(data=True)))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight, font_size=7, alpha=0.7)

    # finds the longest node name to scale nodes to size of text
    node_len = 0
    for i in range(nod_cout):
        if len(nod_list[i]) > node_len:
            node_len = len(nod_list)


    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=node_len * 110, node_shape='h', node_len=100, alpha=0.5)
    # other node_shape to try:   so^>v<dph8 

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=edge, width=2, edge_color='b', alpha=0.5)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')


    plt.axis('off')
    plt.subplots_adjust(left=0.00, bottom=0.00, right=1.00, top=1.00, wspace=0.2, hspace=0.2)
    plt.figure(1, figsize=(1000, 1000))
    plt.show()


file_name = "city-pairs.txt"

# collects a list of all nodes without duplicates
nod_set = set()
with open(file_name) as f:
    for l in f:
        column = l.strip().split(' ')
        nod_set.add(column[0])
        nod_set.add(column[1])
f.close()

nod_list = list(nod_set)  # converts the set to a list
nod_cout = (len(nod_set))  # maintain a count of all nodes

# Build a 2D array that is squared to fit the number of nodes present
gMatrix = [[0 for i in range(nod_cout)]
           for j in range(nod_cout)]

#    Todo: Associate with each vertex v of the graph a number
#     C[v] (the cheapest cost of a connection to v)
#     and an edge E[v] (the edge providing that cheapest connection)..
#    Todo:To initialize these values, set all values of C[v] to +∞
#     (or to any number larger than the maximum edge weight)
#     and set each E[v] to a special flag value indicating that there is no edge connecting v to earlier vertices.
# Fills the 2D array with all entry data found in doc
with open(file_name) as f:
    for l in f:
        column = l.strip().split(' ')
        gMatrix[int(nod_list.index(column[0]))][int(nod_list.index(column[1]))] = int(column[2])
        gMatrix[int(nod_list.index(column[1]))][int(nod_list.index(column[0]))] = int(column[2])
f.close()

# print the matrix
for row in gMatrix:
    for val in row:
        print("{:4}".format(val), end=' ')
    print("\n")

# how to get the 0 flag in the nodes
# starting at 0 0, if you visit 0, 1
# set flag 1, 1 to visited
# if you visit 0, 2 set 2, 2 to visited

# print(column[2])


isVisited: List[bool] = []
for j in range(nod_cout):
    isVisited.append(False)
count = 0
setToReturn = []
mySet = gMatrix

isVisited[0] = True

for z in range(nod_cout):

    minVal: int = pow(2, 61)
    x = 0
    y = 0

    for i in range(nod_cout):
        if isVisited[i]:
            for j in range(nod_cout):
                if not isVisited[j]:
                    if int(minVal) > int(mySet[i][j]):
                        minVal = mySet[i][j]
                        y = j
                        x = i
    print("From:", x, "to", y, "=", mySet[x][y], "\n")
    count += int(mySet[x][y])
    setToReturn.append([x, y, int(mySet[x][y])])
    isVisited[y] = True
print("The total weight:", count)
for row in setToReturn:
        print("From", nod_list[row[0]], "to", nod_list[row[1]], "=", row[2], "miles" )


#
#
#
#######################################################################


display_graph(setToReturn)
