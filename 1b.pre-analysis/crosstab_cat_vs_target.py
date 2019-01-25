def crosstab_cat_vs_target(df,input_cat_col, target_cat_col):
    '''
    AIM    -> Find relationship between two categorical variables (in this case, each categorical input will be inspected with categorical target column)
     
    INPUT  -> df, list of input categorical variables and target variables (only applied in classification problem)
    
    OUTPUT -> significance of each input categorical variables toward target variable 
    ------
    '''
    import scipy.stats
    for col in cat_col:
        cont = pd.crosstab(df[col], df[target_cat_col])
        chi2_stat, p_val, dof, ex = scipy.stats.chi2_contingency(cont)
        print("===" + col +"===")
        print("===P-Value===")
        print(p_val)
        print("\n")
