def tukey_num_vs_cat(df, input_num_col, target_cat_col):
    '''
    AIM    -> Find pairwise between numerical variables and categorical variables after inspecting their relationship with ANOVA (in this case, each numerical input will be inspected with categorical target column)
     
    INPUT  -> df, list of input numerical variables and target variables (only applied in classification problem)
    
    OUTPUT -> pairwise significance of each input numerical variables toward target variable 
    ------
    '''
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    for col in input_num_col:
        tukey = pairwise_tukeyhsd(endog = df[col],    
                                  groups = df[target_cat_col],
                                  alpha = 0.05)
        if len(df[target_cat_col].unique()) > 2:
            tukey.plot_simultaneous(xlabel = col)                      
            print("===" + col +"===")
            print(tukey.summary())
            print("\n")
        else:
            print("===" + col +"===")
            print(tukey.summary())
            print("\n")
