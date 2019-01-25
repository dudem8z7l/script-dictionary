def drop_multiple_col(col_names_list, df): 
    '''
    AIM    -> Drop multiple columns based on their column names 
    
    INPUT  -> List of column names, df
    
    OUTPUT -> updated df with dropped columns 
    ------
    '''
    df.drop(col_names_list, axis=1, inplace=True)
    return df

def change_dtypes(col_int, col_float, col_cat, df): 
    '''
    AIM    -> Changing dtypes to save memory
     
    INPUT  -> List of column names (int, float), df
    
    OUTPUT -> updated df with smaller memory  
    ------
    '''
    df[col_int] = df[col_int].astype('int32')
    df[col_float] = df[col_float].astype('float32')
    df[col_cat] = df[col_cat].astype('category')
    return df
    
def check_missing_data(df):
    '''
    AIM    -> Checking missing data
     
    INPUT  -> df
    
    OUTPUT -> Missing data report 
    ------
    '''
    # check for any missing data in the df (display in descending order)
    return df.isnull().sum().sort_values(ascending=False)

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

def convert_str_datetime(df): 
    '''
    AIM    -> Convert datetime(String) to datetime(format we want)
     
    INPUT  -> df
    
    OUTPUT -> updated df with new datetime format 
    ------
    '''
    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f'))
    return df
