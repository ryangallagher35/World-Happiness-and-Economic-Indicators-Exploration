# Ryan Gallagher 
# World Happiness and Economic Indicators Explorer 
# KMeans and PCA

import os
os.environ["OMP_NUM_THREADS"] = "1"

# Library importing and management.
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from matplotlib.backends.backend_pdf import PdfPages

# Import the master dataset. 
data = pd.read_csv("C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Merged CSV Datasets/master_data.csv")

### Use K-Means to find the ideal number of clusters based on happiness scores and economic indicators using the elbow method. Clustering is conducted for each year from 2020 to 2023.
scaler = StandardScaler()
K_range = range(1, 11)
years = [2020, 2021, 2022, 2023] 
scaled_data = {}

output_path_1 = "C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Graphical Output/KMeans PCA Elbow Charts.pdf"
with PdfPages(output_path_1) as pdf1: 
for year in years: 

    # Declare feature and target data. 
    features = [
        f'Happiness score_{year}',
        f'Logged GDP per capita_{year}', 
        f'Social support_{year}', 
        f'Healthy life expectancy_{year}', 
        f'Freedom to make life choices_{year}', 
        f'Generosity_{year}',
        f'Perceptions of corruption_{year}', 
        f'Internet Users_{year}', 
        f'Education Expenditure_{year}', 
        f'Healthcare Expenditure_{year}', 
        f'Unemployment Rate_{year}', 
        f'Population in Urban Areas_{year}'
    ] 

    data_subset = data[features].dropna()
    scaled_data[year] = scaled_data_subset = scaler.fit_transform(data_subset) 
    
    # Use the elbow method to determine the optimal number of clusters and graph the results. 
    intertias = [] 
    for k in K_range: 
        kmeans = KMeans(n_clusters = k, random_state = 42)
        kmeans.fit(scaled_data_subset) 
        intertias.append(kmeans.inertia_) 

    # Plot the elbow chart.
    plt.plot(K_range, intertias, marker = 'o') 
    plt.xlabel("Number of Clusters") 
    plt.ylabel("Intertia")
    plt.title(f'Elbow Method for Optimal k: {year}') 
    plt.grid(True)
    pdf1.savefig() 
    plt.close()
    plt.show()

# Using the elbow method above, we have found the optimal number of clusters for each year is 4. We will now apply K-Means clustering using k = 4 for each year and visualize the clusters using PCA. 
output_path_2 = "C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Graphical Output/KMeans PCA Clusters.pdf" 
with PdfPages(output_path_2) as pdf2:
    for year in years: 
    
        # Apply K-Means clustering using k = 4.
        kmeans_optimized = KMeans(n_clusters = 4, random_state = 42) 
        clusters = kmeans_optimized.fit_predict(scaled_data[year]) 
        data[f'Cluster_{year}'] = clusters
    
        clusters_labeled = clusters + 1
        
        # Apply PCA transformation for visualization.
        pca = PCA(n_components = 2) 
        pca_result = pca.fit_transform(scaled_data[year]) 
    
        # Plot the results.
        plt.figure(figsize = (8, 6)) 
        scatter = plt.scatter(pca_result[:, 0], pca_result[:, 1], c = clusters_labeled, cmap = 'viridis')
        cbar = plt.colorbar(scatter, ticks = [1, 2, 3, 4]) 
        cbar.set_label('Clusters') 
        cbar.ax.set_yticklabels(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
        plt.title(f'K-Means Clustering Visualized using PCA: {year}')
        plt.xlabel("PCA Component 1") 
        plt.ylabel("PCA Component 2")
        plt.grid(True)
        pdf2.savefig() 
        plt.close() 

# Construct CSV file to store which cluster each country belongs to each year, reflecting the results of the KMeans and PCA cluster plots. 
country_clusters = pd.DataFrame() 

if 'Country Name' in data.columns: 
    country_clusters['Country Name'] = data['Country Name'] 
    
for year in years: 
    cluster_col = f'Cluster_{year}'
    features = [
            f'Happiness score_{year}',
            f'Logged GDP per capita_{year}', 
            f'Social support_{year}', 
            f'Healthy life expectancy_{year}', 
            f'Freedom to make life choices_{year}', 
            f'Generosity_{year}',
            f'Perceptions of corruption_{year}', 
            f'Internet Users_{year}', 
            f'Education Expenditure_{year}', 
            f'Healthcare Expenditure_{year}', 
            f'Unemployment Rate_{year}', 
            f'Population in Urban Areas_{year}'
    ] 

    valid_rows = data[features + ['Country Name']].dropna() 
    year_clusters = valid_rows[['Country Name']].copy() 
    year_clusters[cluster_col] = data.loc[valid_rows.index, cluster_col] 
    country_clusters = country_clusters.merge(year_clusters, on = 'Country Name', how = 'left')

country_clusters = country_clusters.drop_duplicates(subset = 'Country Name') 
output_path_3 = "C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Generated Data/KMeans_Clusters.csv"
country_clusters.to_csv(output_path_3, index = False)
