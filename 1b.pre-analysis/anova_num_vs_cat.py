def anova_num_vs_cat(df, input_num_col, target_cat_col):
    '''
    AIM    -> Find relationship between numerical variables and categorical variables
     
    INPUT  -> df, list of input numerical variables and target variables (only applied in classification problem)
    
    OUTPUT -> significance of each input numerical variables toward target variable 
    ------
    '''
    for col in input_num_col:
        group = []
        for target_cat in df[target_cat_col].unique():
            group.append(np.array(df[col][df[target_cat_col] == target_cat]))
        f_val, p_val = stats.f_oneway(*group)
        print('COLUMN: {}, p-value: {}'.format(col, p_val))
