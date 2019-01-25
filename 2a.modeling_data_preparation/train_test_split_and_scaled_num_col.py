def train_test_split_and_scaled_num_col(df_model, input_col, target_col):
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split
    
    #train test split
    X_train, X_test, y_train, y_test = train_test_split(df[input_col], df[target_col], test_size=0.4, random_state=1)
    
    # min max scaled for numerical columns
    scaler = preprocessing.MinMaxScaler()
    # fit transform on train dataset
    X_train[X_train.select_dtypes(include=['float', 'integer']).columns] = scaler.fit_transform(X_train[X_train.select_dtypes(include=['float', 'integer']).columns])
    # only transform on test dataset
    X_test[X_test.select_dtypes(include=['float', 'integer']).columns] = scaler.transform(X_test[X_test.select_dtypes(include=['float', 'integer']).columns])
    
    return scaler, X_train, X_test