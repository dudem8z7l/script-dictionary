def plot_b_o_distribution(df,feature,color,bins=100):
    plt.figure(figsize=(10,6))
    plt.title("Distribution of %s" % feature)
    x = df[feature].dropna()
    filtered = x[~is_outlier(x)]
    sns.distplot(filtered,color=color, kde=True,bins=bins)
    plt.show() 
