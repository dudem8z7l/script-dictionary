def h2oautoml_binary_classification(X_train, y_train, X_test, y_test, target_col):
    '''
    AIM    -> Performing H2O automl
     
    INPUT  -> X_train, y_train, X_test, y_test, target_col = target column
    
    OUTPUT -> Best model according to automl
    ------
    '''
    import h2o
    from h2o.automl import H2OAutoML
    
    df_train = X_train.copy()
    df_train[target_col] = y_train.values
    df_test = X_test.copy()
    df_test[target_col] = y_test.values
    
    htrain = h2o.H2OFrame(df_train)
    htest = h2o.H2OFrame(df_test)
    htrain[target_col] = htrain[target_col].asfactor()
    htest[target_col] = htest[target_col].asfactor()
    
    aml = H2OAutoML(max_models = 300, seed=1)
    aml.train(x = list(X_train.columns), y = 'STATUS', training_frame = htrain, validation_frame = htest)
    return aml
