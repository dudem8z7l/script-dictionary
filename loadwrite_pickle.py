def writetopickle(filename, obj):
    '''
    AIM    -> convert object to pickle
     
    INPUT  -> output filename and object to be converted
    
    OUTPUT -> pickle object
    ------
    '''
    import pickle
    f = open('./{}'.format(filename),'wb')
    pickle.dump(obj,f)
    f.close()
    return

def load_from_pickle(fname):
    '''
    AIM    -> load pickle object
     
    INPUT  -> filename
    
    OUTPUT -> desire object
    ------
    '''
    import pickle
    f = open(fname,'rb')
    return pickle.load(f)
