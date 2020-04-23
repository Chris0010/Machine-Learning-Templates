# Hierarchical Clustering

# Call libraries
import pandas as pd
import matplotlib.pyplot as plt

# import the dataset
dataset = pd.read_csv()
X =

# Dendrogram to find the number of clusters that optimizes the algorithm
import scipy.cluster.hierarchy as sch
# the ward method minimizes the variance within each cluster
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))

# Visualize the result
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance')
plt.show()

# Fit clustering to dataset
from sklearn.cluster import AgglomerativeClustering
# n_clusters that were found in the Dendrogram, affinity is default 'euclidean', and linkage is default 'ward'
hc = AgglomerativeClustering(n_clusters = 5)
y_hc = hc.fit_predict(X)

# Visualize the HC in 2 dimensions, if higher dimensions you must reduce the dimensions to 2
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.show()
