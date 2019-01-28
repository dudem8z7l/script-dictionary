def KPrototypes_cluster(input_data, k_clusters):
  from kmodes.kprototypes import KPrototypes
  #normalized data
  normalized = preprocessing.StandardScaler()
  input_data[input_data.select_dtypes(include=['float', 'integer']).columns] = normalized.fit_transform(input_data[input_data.select_dtypes(include=['float', 'integer']).columns])
  input_data = input_data.as_matrix()

  kproto = KPrototypes(n_clusters = k_clusters, init='Cao', verbose=2)
  clus_kmeans_fit = kproto.fit_predict(input_data, categorical = [0,1,2,3,4,5,6,7])
  return(clus_kmeans_fit)
