def kmeans_cluster(input_data, k_clusters):
    from sklearn.cluster import KMeans
    normalized = preprocessing.StandardScaler()
    input_data = normalized.fit_transform(input_data)
    data_normalized = pd.DataFrame(input_data)
    
    clus_kmeans = KMeans(n_clusters = k_clusters, n_init = 200)
    clus_kmeans_fit = clus_kmeans.fit(data_normalized)
    labels = clus_kmeans_fit.predict(data_normalized)
    return(labels)
