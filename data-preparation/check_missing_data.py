def check_missing_data(df):
    '''
    AIM    -> Checking missing data
     
    INPUT  -> df
    
    OUTPUT -> Missing data report 
    ------
    '''
    # check for any missing data in the df (display in descending order)
    return df.isnull().sum().sort_values(ascending=False)
