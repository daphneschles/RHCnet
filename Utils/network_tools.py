import tensorflow.keras.backend as K
from tensorflow.keras.models import load_model
import pickle
import sys
import numpy as np
sys.path.append('..')
sys.path.append('../Utils')
sys.path.append('../Models')

from hnet import *

from tensorflow_addons.optimizers import RectifiedAdam

default_model_loc = '../SavedModels/trained_model/best_val_weights.pkl'
default_pretrained_model_loc = '../SavedModels/ecg_supervised_416.h5'


def pearson(y_true, y_pred):
    # normalizing stage - setting a 0 mean.
    y_true -= K.mean(y_true, axis=-1)
    y_pred -= K.mean(y_pred, axis=-1)
    # normalizing stage - setting a 1 variance
    y_true = K.l2_normalize(y_true, axis=-1)
    y_pred = K.l2_normalize(y_pred, axis=-1)
    # final result
    pearson_correlation = K.sum(y_true * y_pred, axis=-1)
    return pearson_correlation


def save_weights(model, save_loc) :
    w = model.get_weights()
    file = open(save_loc, 'wb')
    pickle.dump(w, file)
    file.close()

def load_weights(model, model_loc=default_model_loc) :

    model.build((None,5000,12))

    with open(model_loc, 'rb') as file:
        w = pickle.load(file)
    file.close()
    
    model.set_weights(w)
    
    return model

def load_pretrained_model(pre_trained_loc=default_pretrained_model_loc) :
    pre_trained_model = load_model(pre_trained_loc, custom_objects={
            'swish': tf.nn.swish,
            'RectifiedAdam': RectifiedAdam,
            'pearson': pearson,
        })
    
    return pre_trained_model

def make_final_net(pre_trained_loc=default_pretrained_model_loc, model_loc=default_model_loc) :
    pre_trained_model = load_pretrained_model(pre_trained_loc=pre_trained_loc)
    latent = tf.keras.Model(pre_trained_model.inputs, pre_trained_model.get_layer('embed').output)
    full_model = AppendNet(latent)
    
    full_model = load_weights(full_model, model_loc=model_loc)
    
    return full_model


'''
Pre-process an array of ECGs of shape  N_ECGs x N_samples x 1
N_samples is the number of samples in a single ECG
'''
def pre_process_ECG(ecg) :
    
    # first, normalize each signal 
    ecg_norm = (ecg - ecg.mean(axis=0))/ecg.std(axis=0)
    ecg_norm = np.expand_dims(ecg_norm, 2)
    
    # tile the signal so it is the right shape for the model
    ecg_tile = np.tile(ecg_norm, [1,1,12])
    
    return ecg_tile
    