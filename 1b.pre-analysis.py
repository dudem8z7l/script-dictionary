def correlation_matrix(df):
    '''
    AIM    -> Find linear correlation between two numerical variables
     
    INPUT  -> df
    
    OUTPUT -> correlation matrix between numerical variables
    ------
    '''
    corr = df.corr()
    corr.style.background_gradient()

def crosstab_cat_vs_cat(df,input_cat_col, target_cat_col):
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
        tukey.plot_simultaneous(xlabel = col)                      
        print("===" + col +"===")
        print(tukey.summary())
        print("\n")
