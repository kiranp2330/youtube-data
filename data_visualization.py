import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Load centrality metrics
metrics = pd.read_csv('centrality_metrics.csv')

# Plot Degree Centrality
plt.figure(figsize=(10, 5))
plt.bar(metrics['channel_id'], metrics['degree_centrality'], color='b')
plt.title('Degree Centrality of YouTube Channels')
plt.xlabel('Channel ID')
plt.ylabel('Degree Centrality')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('degree_centrality.png')
plt.show()

# Plot Betweenness Centrality
plt.figure(figsize=(10, 5))
plt.bar(metrics['channel_id'], metrics['betweenness_centrality'], color='g')
plt.title('Betweenness Centrality of YouTube Channels')
plt.xlabel('Channel ID')
plt.ylabel('Betweenness Centrality')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('betweenness_centrality.png')
plt.show()

# Load the graph and visualize
G = nx.read_gpickle('youtube_graph.gpickle')  # Load the graph

# Draw the network graph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title('YouTube Channel Collaboration Network')
plt.savefig('youtube_network_graph.png')
plt.show()
