def convert_cat2num(df, transform_dict):
    '''
    AIM    -> convert categorical variable to numerical variable
     
    INPUT  -> df
    
    OUTPUT -> updated df with its categorical variable converted to numerical 
    ------
    '''
    for col in transform_dict.keys():
        df[col] = df[col].map(transform_dict[col])
    return df
