# Plot distribution of multiple features, with TARGET = 1/0 on the same graph
def plot_distribution_comp(df, target_col, var,nrow=2):
    rare_target = df[target_col].value_counts(ascending = True).index[0]
    t1 = df.loc[df[target_col] == rare_target]
    t0 = df.loc[df[target_col] != rare_target]

    sns.set_style('whitegrid')
    plt.figure()
    fig, ax = plt.subplots(nrow,2,figsize=(12,6*nrow))
    
    i = 0
    for feature in var:
        i += 1
        plt.subplot(nrow,2,i)
        sns.kdeplot(t1[feature], bw=0.5,label="{} = {}".format(target_col, rare_target))
        sns.kdeplot(t0[feature], bw=0.5,label="{} != {}".format(target_col, rare_target))
        plt.ylabel('Density plot', fontsize=12)
        plt.xlabel(feature, fontsize=12)
        locs, labels = plt.xticks()
        plt.tick_params(axis='both', which='major', labelsize=12)
    plt.show();
