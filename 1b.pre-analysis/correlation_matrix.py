def correlation_matrix(df):
    '''
    AIM    -> Find linear correlation between two numerical variables
     
    INPUT  -> df
    
    OUTPUT -> correlation matrix between numerical variables
    ------
    '''
    corr = df.corr()
    corr.style.background_gradient()
