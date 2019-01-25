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
