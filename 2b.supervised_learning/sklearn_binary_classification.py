def sklearn_binary_classification(X_train, y_train, scoring = 'accuracy'):
    '''
    AIM    -> First 'screening' for binary classification prediction using cross validation for several in sklearn
     
    INPUT  -> X_train, y_train
    
    OUTPUT -> evaluation scoring for each model
    ------
    '''
    from sklearn.model_selection import KFold, cross_val_score
    
    from sklearn.naive_bayes import BernoulliNB, GaussianNB
    from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
    from sklearn.svm import LinearSVC, SVM
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
