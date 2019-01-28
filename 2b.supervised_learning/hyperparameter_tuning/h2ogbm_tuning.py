def h2ogbm_tuning():
  #Create Base Model
  gbm = H2OGradientBoostingEstimator(
    ntrees = 10000,                                                            
    learn_rate = 0.01,                                                         
    stopping_rounds = 5, stopping_tolerance = 1e-4, stopping_metric = "AUC", 
    sample_rate = 0.8,                                                       
    col_sample_rate = 0.8,
    calibration_frame = htest,
    seed = 1234,                                                             
    score_tree_interval = 10)
    
  gbm.train(x = input_col, y = target_col, training_frame = htrain, validation_frame = htest)
  perf_gbm = gbm.model_performance(htest)
  print('Base Model Evaluation')
  print('AUC : {}'.format(perf_gbm.auc()))
  print('Logloss : {}'.format(perf_gbm.logloss()))
  print('Accuracy : {}'.format(perf_gbm.accuracy()))
  
  #Hyperparameter Tuning
  hyper_params = {'max_depth' : [4,6,8,12,16,20]}

  gbm_grid = H2OGradientBoostingEstimator(
      ntrees=10000,
      learn_rate=0.05,
      learn_rate_annealing = 0.99,
      sample_rate = 0.8,
      col_sample_rate = 0.8,
      calibration_frame = htest,
      seed = 1234,
      score_tree_interval = 10, 
      stopping_rounds = 5,
      stopping_metric = "AUC",
      stopping_tolerance = 1e-4)

  grid = H2OGridSearch(gbm_grid, hyper_params,
                           grid_id = 'depth_grid_tele',
                           search_criteria = {'strategy': "Cartesian"})
  grid.train(x = input_col, y = target_col, training_frame = htrain, validation_frame = htest)
  sorted_grid = grid.get_grid(sort_by='auc',decreasing=True)
  max_depths = sorted_grid.sorted_metric_table()['max_depth'][0:2]
  new_max = int(max(max_depths, key=int))
  new_min = int(min(max_depths, key=int))
  
  hyper_params_tune = {'max_depth' : list(range(new_min,new_max+1,1)),
                     'sample_rate': [x/100. for x in range(20,101)],
                     'col_sample_rate' : [x/100. for x in range(20,101)],
                     'col_sample_rate_per_tree': [x/100. for x in range(20,101)],
                     'col_sample_rate_change_per_level': [x/100. for x in range(90,111)],
                     'min_rows': [2**x for x in range(0,int(math.log(htrain.nrow,2)-1)+1)],
                     'nbins': [2**x for x in range(4,11)],
                     'nbins_cats': [2**x for x in range(4,13)],
                     'min_split_improvement': [0,1e-8,1e-6,1e-4],
                     'histogram_type': ["UniformAdaptive","QuantilesGlobal","RoundRobin"]}

  search_criteria_tune = {'strategy': "RandomDiscrete",
                          'max_runtime_secs': 3600,  ## limit the runtime to 60 minutes
                          'max_models': 100,  ## build no more than 100 models
                          'seed' : 1234,
                          'stopping_rounds' : 5,
                          'stopping_metric' : "AUC",
                          'stopping_tolerance': 1e-3
                         }
  gbm_grid = H2OGradientBoostingEstimator(distribution='bernoulli',
                                              ntrees=10000,
                                              learn_rate=0.05,
                                              learn_rate_annealing = 0.99,      
                                              score_tree_interval = 10,                                                  
                                              calibration_frame = htest,                                              
                                              seed = 1234,
                                              stopping_rounds = 5,
                                              stopping_metric = "AUC",
                                              stopping_tolerance = 1e-4)

  grid = H2OGridSearch(gbm_grid, hyper_params = hyper_params_tune,
                             grid_id = 'depth_grid',
                             search_criteria = search_criteria_tune)
  grid.train(x = input_col, y = target_col, training_frame = htrain, validation_frame = htest)
  sorted_final_grid = grid.get_grid(sort_by='auc',decreasing=True)
  
  best_model = h2o.get_model(sorted_final_grid.sorted_metric_table()['model_ids'][0])
  performance_best_model = best_model.model_performance(htest)
  print('Hyperparameter Tuning Evaluation')
  print('AUC : {}'.format(performance_best_model.auc()))
  print('Logloss : {}'.format(performance_best_model.logloss()))
  print('Accuracy : {}'.format(performance_best_model.accuracy()))
  print('Variable Importance')
  print(best_model.varimp(use_pandas=True).head(10))
  print(best_model.confusion_matrix(valid=htest))
  return best_model
