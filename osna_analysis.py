# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation as ap


listeOfName=[]

############################################################################################################
####################################  Extraction of the data : #################################################################
############################################################################################################
""" 
In this part, we collect the data from the social network.
The data are download in two files (the first 100 users have a different file
because at the begining we download it ina json file, and we have converted it 
after) 
"""


M=open("twitter_user_data1.txt","r")
for x in M:
    A=x.split("{")
    for B in range(len(A)):
        C=A[B].split('"')      #In these two loops, we only want to take the names of the users
        if len(C)>7:
            listeOfName.append(C[7])   #we put the names in the list listeOfName[]
M.close()

M2=open("twitter_user_data2.txt","r")
for x in M2:
    x.strip()
    A=x.split('"')
    if len(A)>4 and A[1]=="name":
        listeOfName.append(A[3])
M2.close()

number=len(listeOfName)     # this is the number of followers in our graph
 


############################################################################################################
################# Creation of the graph :  ######################################################################## 
############################################################################################################

fig, ax = plt.subplots(figsize=(50,50))
G = nx.Graph()


######################### Nodes :  ############################################

couleur=['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']
color_map = []          # this list of colors is only usefull to make the graph looks cool

for x in range(number+1):       #creation of the 300 followers/nodes
    G.add_node(x)
    color_map.append(couleur[x%len(couleur)])
    
    
######################### Edges :  ############################################

# in this graph, the only edges are between the main character (node number 0) and each followers
for x in range(1,number+1):         
    G.add_edges_from([(0, x)])


######################### Labels :  ############################################

lab = {}
lab[0]="Ivanka Trump"       # the main user is Ivanka Trump
for x in range(number):
    lab[x+1]=listeOfName[x]    


######################### Size :  ############################################

size=[50000]                                    # we make the main node bigger than the others
[size.append(3000) for k in range(number)]


######################### Graph :  ############################################

nx.spring_layout(G)
nx.draw_networkx(G, node_color=color_map, labels=lab, with_labels = True, node_size=[v for v in size])
    
#print(G.size())



############################################################################################################
#################################### Calculation :  ########################################################################
############################################################################################################

#Degree Distribution 
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
dmax = max(degree_sequence)
fig = plt.figure("Degree of the graph", figsize=(8, 8))
axgrid = fig.add_gridspec(5, 4)

ax1 = fig.add_subplot(axgrid[3:, :2])
ax1.plot(degree_sequence, "b", marker="o")
ax1.set_title("Degree Distribution")
ax1.set_ylabel("frequency")
ax1.set_xlabel("in-degree")

fig.tight_layout()
plt.show()


#Clustering Coefficient, 
#print(nx.triangles(G))
print("Clustering Coefficient :",nx.average_clustering(G))

#Pagerank, 
print("Pagerank :",nx.pagerank(G,alpha=0.9))

#Diameter, 
print("Diameter :",nx.diameter(G))

#Closeness, 
print("Closeness Centrality :",nx.closeness_centrality(G))

#Betweeness
print("Betweeness Centrality :",nx.betweenness_centrality(G))

#density,
print("Density :", nx.density(G))

#Metric closure :
print("Metric closure :", ap.metric_closure(G))

#Ramsay numbers :
#print("Ramsay numbers :", ap.ramsey_R2(G))


