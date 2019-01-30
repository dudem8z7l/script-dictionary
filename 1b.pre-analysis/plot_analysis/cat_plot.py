def cat_plot(data, target_col, plot_title):
    temp = data[target_col].value_counts()
    df = pd.DataFrame({'labels': temp.index,
                       'values': temp.values
                      })
    plt.figure(figsize = (6,6))
    plt.title(plot_title)
    sns.set_color_codes("pastel")
    sns.barplot(x = 'labels', y="values", data=df)
    locs, labels = plt.xticks()
    plt.show()
