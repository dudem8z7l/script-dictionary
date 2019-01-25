def boxplot_binary_classification(results, names):
    '''
    AIM    -> Boxplot for evaluating model performance
     
    INPUT  -> results : list of array resulted from cross validation output; names : name of model used
    
    OUTPUT -> boxplot for each model
    ------
    '''
    import matplotlib.pyplot as plt
    
    # boxplot algorithm comparison
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()
