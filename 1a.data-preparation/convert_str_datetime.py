def convert_str_datetime(df): 
    '''
    AIM    -> Convert datetime(String) to datetime(format we want)
     
    INPUT  -> df
    
    OUTPUT -> updated df with new datetime format 
    ------
    '''
    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f'))
    return df
