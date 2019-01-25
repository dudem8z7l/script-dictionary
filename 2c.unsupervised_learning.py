def kmeans_cluster(input_data, k_clusters):
    from sklearn.cluster import KMeans
    normalized = preprocessing.StandardScaler()
    input_data = normalized.fit_transform(input_data)
    data_normalized = pd.DataFrame(input_data)
    
    clus_kmeans = KMeans(n_clusters = k_clusters, n_init = 200)
    clus_kmeans_fit = clus_kmeans.fit(data_normalized)
    labels = clus_kmeans_fit.predict(data_normalized)
    return(labels)

def evaluate_k_means_cluster_with_ground_truth(df, input_num_col, input_range = range(2,11), ground_truth_col):
    from sklearn.metrics import homogeneity_score, completeness_score, v_measure_score
    v_score = []
    hg_score = []
    cp_score = []
    for i in input_range:
        Cluster = kmeans_cluster(df[input_num_col], i)
        v_score.append(v_measure_score(df[ground_truth_col], Cluster))
        hg_score.append(homogeneity_score(df[ground_truth_col], Cluster))
        cp_score.append(completeness_score(df[ground_truth_col], Cluster))
