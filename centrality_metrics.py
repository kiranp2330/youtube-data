mport networkx as nx
import pandas as pd

# Load the graph
G = nx.read_gpickle('youtube_graph.gpickle')  # Assuming you've saved the graph

# Calculate centrality metrics
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Compile results
metrics = pd.DataFrame({
    'channel_id': list(degree_centrality.keys()),
    'degree_centrality': list(degree_centrality.values()),
    'betweenness_centrality': list(betweenness_centrality.values()),
    'eigenvector_centrality': list(eigenvector_centrality.values())
})

# Save metrics to CSV
metrics.to_csv('centrality_metrics.csv', index=False)
print("Centrality metrics calculated and saved 'centrality_metrics.csv'.")
