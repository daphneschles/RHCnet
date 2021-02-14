import tensorflow.keras.backend as K
import pickle

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

def load_weights(model, save_loc) :

    model.build((None,5000,12))

    with open(save_loc, 'rb') as file:
        w = pickle.load(file)
    file.close()
    
    model.set_weights(w)
    
    return model