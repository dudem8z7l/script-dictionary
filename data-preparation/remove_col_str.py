def remove_col_str(df, col, string = '\n'):
    '''
    AIM    -> Remove strings in given columns
     
    INPUT  -> df, string/list of columns, string that want to be removed
    
    OUTPUT -> df with removed unwanted string
    ------
    '''
    # remove a portion of string in a dataframe column - col_1
    df[col].replace(string, '', regex=True, inplace=True)
    return df
