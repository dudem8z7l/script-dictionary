def evaluate_cluster_with_ground_truth(df, algo = kmeans_cluster, input_col, input_range = range(2,11), ground_truth_col):
    from sklearn.metrics import homogeneity_score, completeness_score, v_measure_score
    v_score = []
    hg_score = []
    cp_score = []
    for i in input_range:
        Cluster = algo(df[input_col], i)
        v_score.append(v_measure_score(df[ground_truth_col], Cluster))
        hg_score.append(homogeneity_score(df[ground_truth_col], Cluster))
        cp_score.append(completeness_score(df[ground_truth_col], Cluster))
