import json
import pickle
import numpy as np

__data_columns= None
__model=None

def get_estimated_price(sqft,baths, beds):
    #x is numpy array
    #similar like Code in Jupyter Notebook
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = baths
    x[2] = beds
    #array has one element, so we take the first element
    #round answer
    return round(__model.predict([x])[0],2)

def get_feature_names():
    return __features


def load_saved_artifacts():
    print('loading saved artifacts')
    global __data_columns
    global __features

    # load json file
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns=json.load(f)['data']
        __features=__data_columns[0:]

    global __model
    #load pickle file
    with open('./artifacts/san_diego_price_model.pickle', 'rb') as f:
        __model=pickle.load(f)
    print('loading saved artifacts..done')
if __name__== '__main__':
    load_saved_artifacts()
    print(get_feature_names())
    print(get_estimated_price(1000, 2, 3))
    print(get_estimated_price(1500, 1, 2))