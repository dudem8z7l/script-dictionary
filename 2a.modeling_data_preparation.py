def inverse_transform_cat_dict(df):
    '''
    AIM    -> Build inverse and transform dictionary for categorical variables
     
    INPUT  -> df
    
    OUTPUT -> inverse and transform dictionary 
    ------
    '''
    #convert categorical variable to numerical variable
    inverse_dict = {col: {n: cat for n, cat in enumerate(df.select_dtypes(include=['category'])[col].cat.categories)} for col in df.select_dtypes(include=['category'])}
    
    #fit transform dictionary (cat to int)
    transform_dict = {col: dict((v,k) for k,v in inverse_dict[col].items()) for col in df.select_dtypes(include=['category'])}
    return inverse_dict, transform_dict

def convert_cat2num(df, transform_dict):
    '''
    AIM    -> convert categorical variable to numerical variable
     
    INPUT  -> df
    
    OUTPUT -> updated df with its categorical variable converted to numerical 
    ------
    '''
    for col in df.select_dtypes(include=['category']).columns:
        df[col] = df[col].map(transform_dict[col])
    return df

def get_dummies(df):
    '''
    AIM    -> convert dataframe to dummy variable
     
    INPUT  -> df
    
    OUTPUT -> updated df with dummy variable in its categorical variables
    ------
    '''
    df = pd.get_dummies(df[input_cat_col + input_num_col])
    return df

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

def writetopickle(filename, obj):
    '''
    AIM    -> convert object to pickle
     
    INPUT  -> output filename and object to be converted
    
    OUTPUT -> pickle object
    ------
    '''
    import pickle
    f = open('./{}'.format(filename),'wb')
    pickle.dump(obj,f)
    f.close()
    return

def load_from_pickle(fname):
    '''
    AIM    -> load pickle object
     
    INPUT  -> filename
    
    OUTPUT -> desire object
    ------
    '''
    import pickle
    f = open(fname,'rb')
    return pickle.load(f)
