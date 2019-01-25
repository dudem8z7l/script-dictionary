def sklearn_binary_classification(X_train, y_train, scoring = 'accuracy'):
    from sklearn.model_selection import KFold, cross_val_score
    
    from sklearn.naive_bayes import BernoulliNB, GaussianNB
    from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
    from sklearn.svm import LinearSVC
    from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
    from sklearn.neural_network import MLPClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    
    # prepare configuration for cross validation test harness
    seed = 7
    # prepare models
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    models.append(('GBM', GradientBoostingClassifier(n_estimators=1000)))
    models.append(('RF', RandomForestClassifier(n_estimators=1000)))
    models.append(('NN', MLPClassifier(alpha = 1)))
    models.append(('ExtraTree', ExtraTreeClassifier()))
    models.append(('ExtraTrees', ExtraTreesClassifier()))
    models.append(('Linear SVM', LinearSVC()))
    models.append(('LR CV', LogisticRegressionCV()))

    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
        kfold = KFold(n_splits=10, random_state=seed)
        cv_results = cross_val_score(model, X_train, y_train, cv = kfold, scoring = scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)
    return results, names
    
def boxplot_binary_classification(results, names):
    import matplotlib.pyplot as plt
    
    # boxplot algorithm comparison
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()

def h2oautoml_binary_classification(X_train, y_train, X_test, y_test, target_col):
    import h2o
    from h2o.automl import H2OAutoML
    
    df_train = X_train.copy()
    df_train[target_col] = y_train.values
    df_test = X_test.copy()
    df_test[target_col] = y_test.values
    
    htrain = h2o.H2OFrame(df_train)
    htest = h2o.H2OFrame(df_test)
    htrain[target_col] = htrain[target_col].asfactor()
    htest[target_col] = htest[target_col].asfactor()
    
    aml = H2OAutoML(max_models = 300, seed=1)
    aml.train(x = list(X_train.columns), y = 'STATUS', training_frame = htrain, validation_frame = htest)
    return aml
