def plot_stats(df, feature, target_col, label_rotation=False, horizontal_layout=True):
    '''
    AIM    -> Plot selected feature overall and compare with rare target class
     
    INPUT  -> df, feature, target_col
    
    OUTPUT -> Plot
    ------
    '''
    temp = df[feature].value_counts() / len(df)
    df1 = pd.DataFrame({feature: temp.index, 'Overall Percentage': temp.values})

    # Calculate the percentage of target=1 per category value
    rare_target = df[target_col].value_counts(ascending = True).index[0]
    cat_perc = (df[df[target_col] == rare_target][[target_col, feature]].groupby(feature).count() / len(df)).reset_index()
    cat_perc.sort_values(by = target_col, ascending=False, inplace=True)
    
    if(horizontal_layout):
        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(14,6))
    else:
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(14,14))
    sns.set_color_codes("pastel")
    s = sns.barplot(ax = ax1, x = feature, y = "Overall Percentage", order = df1[feature], data = df1)
    if(label_rotation):
        s.set_xticklabels(s.get_xticklabels(),rotation=90)
    
    s = sns.barplot(ax = ax2, x = feature, y = target_col, order = cat_perc[feature], data = cat_perc)
    if(label_rotation):
        s.set_xticklabels(s.get_xticklabels(),rotation=90)
    plt.ylabel('Percent of target with value {} [%]'.format(rare_target), fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show();
