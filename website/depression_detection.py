import pickle
import os
import pandas

def get_status(feats):
    modulePath = os.path.dirname(__file__)  # get current directory
    filename = os.path.join(modulePath, 'finalized_model.sav')
    loaded_model = pickle.load(open(filename, 'rb'))

    feat_cols = ['PFQ090', 'INQ060', 'DBQ197', 'CBD071', 'WHQ225', 'CBQ596', 'MCQ300C', 'MCQ160F', 'INQ150', 'DMDMARTL', 'SDMVSTRA', 'AUQ054', 'CBD091', 
    'HUQ071', 'DLQ150', 'HSAQUEX', 'HUQ010', 'INQ140', 'DLQ020', 'MCQ160L', 'FSD032B', 'MIALANG', 'DLQ140', 'RIDRETH1', 'DBD910']
    df = pandas.DataFrame([feat_cols])
    df = df.reindex(columns=feat_cols)
    X = df.loc[:, feat_cols].values
    res = loaded_model.predict(X)
    if res == 1:
        return 'Depressed'
    return 'Not Depressed'