# -*- coding: utf-8 -*-
"""
Twitter Social Network Analysis
This script analyzes a Twitter user's social network by visualizing and computing various graph metrics.
"""

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation as ap

# Initialize an empty list to store names of followers
listeOfName = []

############################################################################################################
# Data Extraction: Extract names of users from two text files
############################################################################################################
"""
In this section, we collect the data from the social network.
The data is stored in two text files: 
- The first file contains 100 users, initially in JSON format, which was later converted.
- The second file contains the remaining users.
"""

# Process twitter_user_data1.txt
with open("twitter_user_data1.txt", "r") as file1:
    for line in file1:
        parts = line.split("{")
        for part in parts:
            subparts = part.split('"')  # Extract names of users
            if len(subparts) > 7:
                listeOfName.append(subparts[7])  # Append names to the list

# Process twitter_user_data2.txt
with open("twitter_user_data2.txt", "r") as file2:
    for line in file2:
        line = line.strip()
        parts = line.split('"')
        if len(parts) > 4 and parts[1] == "name":
            listeOfName.append(parts[3])

# Count the total number of followers
number = len(listeOfName)

############################################################################################################
# Graph Creation: Construct a graph representing the social network
############################################################################################################

# Initialize a matplotlib figure
fig, ax = plt.subplots(figsize=(50, 50))
G = nx.Graph()  # Create an empty graph

# Define a color palette for nodes
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
          'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
color_map = []  # List of colors to make the graph visually appealing

# Add nodes (300 followers and the main user)
for i in range(number + 1):
    G.add_node(i)
    color_map.append(colors[i % len(colors)])

# Add edges: The main user (node 0) connects to all followers
for i in range(1, number + 1):
    G.add_edges_from([(0, i)])

# Add labels for nodes
labels = {0: "Ivanka Trump"}  # Main user
for i in range(number):
    labels[i + 1] = listeOfName[i]  # Followers

# Define node sizes (main user is larger)
sizes = [50000]  # Main user's size
[sizes.append(3000) for _ in range(number)]  # Follower node sizes

# Draw the graph
nx.spring_layout(G)
nx.draw_networkx(G, node_color=color_map, labels=labels, with_labels=True, node_size=sizes)

############################################################################################################
# Graph Analysis: Compute various metrics
############################################################################################################

# Degree Distribution
degree_sequence = sorted([d for _, d in G.degree()], reverse=True)
fig = plt.figure("Degree Distribution", figsize=(8, 8))
plt.plot(degree_sequence, "b", marker="o")
plt.title("Degree Distribution")
plt.ylabel("Frequency")
plt.xlabel("In-Degree")
plt.show()

# Compute various graph metrics
print("Clustering Coefficient:", nx.average_clustering(G))
print("Pagerank:", nx.pagerank(G, alpha=0.9))
print("Diameter:", nx.diameter(G))
print("Closeness Centrality:", nx.closeness_centrality(G))
print("Betweenness Centrality:", nx.betweenness_centrality(G))
print("Density:", nx.density(G))
print("Metric Closure:", ap.metric_closure(G))
