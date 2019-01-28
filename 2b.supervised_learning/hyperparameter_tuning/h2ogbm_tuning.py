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
  
  hyper_params = {'max_depth' : [4,6,8,12,16,20]}

  gbm_grid_tele = H2OGradientBoostingEstimator(
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

  grid_tele = H2OGridSearch(gbm_grid_tele, hyper_params,
                           grid_id = 'depth_grid_tele',
                           search_criteria = {'strategy': "Cartesian"})
