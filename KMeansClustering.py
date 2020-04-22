# K-Means Clustering

# Call libraries
import pandas as pd
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv()
X =

# Call the sklearn library for K-Means Clustering
from sklearn.cluster import KMeans
# create a list for Within Cluster Sum of Squares
wcss = []
for i in range(1, 11):
    # assign the classifier, kmeans ++ is the default init, 300 is the default max_iter, 10 is the default n_init
    kmeans = KMeans(n_clusters = i)
    # fit the classifier to X
    kmeans.fit(X)
    # Use kmeans.inertia_ to compute the wcss and append it to our empty list
    wcss.append(kmeans.inertia_)
# visualize the heuristic Elbow method that was created to truncate the number of clusters
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Apply K-Means to dataset using the number of n_clusters determined by the above elbow method
kmeans = KMeans(n_clusters = 5)
y_kmeans = kmeans.fit_predict(X)

# Visualize the K-Means clustering with the centroids
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.show()