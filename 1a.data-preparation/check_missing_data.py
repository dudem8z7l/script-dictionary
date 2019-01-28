def check_missing_data(df):
    '''
    AIM    -> Checking missing data
     
    INPUT  -> df
    
    OUTPUT -> Missing data report 
    ------
    '''
    # check for any missing data in the df (display in descending order)
    total = data.isnull().sum().sort_values(ascending = False)
    percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
    return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
