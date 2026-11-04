# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Load dataset
data = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# Select numerical columns
X = data.select_dtypes(include=["int64", "float64"])

# Handle missing values
X = X.fillna(X.mean())

# Scale data
sc = StandardScaler()
X_scaled = sc.fit_transform(X)

# Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data["KMeans_Cluster"] = kmeans.fit_predict(X_scaled)

print("K-Means Clustering")
print(data["KMeans_Cluster"].value_counts())

# Hierarchical Clustering - Dendrogram
Z = linkage(X_scaled[:100], method="ward")

plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()

# Agglomerative Clustering
hc = AgglomerativeClustering(n_clusters=3, linkage="ward")
data["Hierarchical_Cluster"] = hc.fit_predict(X_scaled)

print("\nHierarchical Clustering")
print(data["Hierarchical_Cluster"].value_counts())
