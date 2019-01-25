def remove_col_white_space(df,col):
    '''
    AIM    -> Remove whitespace in columns
     
    INPUT  -> df, string/list of columns
    
    OUTPUT -> df with removed whitespace
    ------
    '''
    # remove white space at the beginning of string 
    df[col] = df[col].str.lstrip()
    return df
