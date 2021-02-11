import numpy as np
from tqdm import tqdm
import sys

import tensorflow as tf
from tensorflow import math as tfm

sys.path.append('..')


# set the random seed
SEED_VALUE = 0

'''
Append additional dnese layers to a given pre-trained set of layers
'''
class AppendNet(keras.Model) :
    def __init__(self, 
        pretrained_model, 
        new_layers = [64,48,24,4], 
        dout_rate = 0.5,
        act_f = tf.nn.relu, 
        training = True) :

        super(AppendNet, self).__init__()

        self.pretrained_model = pretrained_model
        self.act_f = act_f

        self.dense_layers = []
        self.dropout_layers = []

        # if the model is being instantiated for inference alone, 
        # there shoould
        if training :
            continue
        else :
            dout = 0

        for d in new_layers :
            self.dense_layers.append(tf.keras.layers.Dense(d))
            self.dropout_layers.append(tf.keras.layers.Dropout(dout, seed=SEED_VALUE))


    def call(self, x) :
        y = self.pretrained_model(x)

        for i in range(len(self.dense_layers)) :
            y = self.act_f(y)
            y = self.dense_layers[i](y)
            y = self.dropout_layers[i](y)

        # sigmoid activation function on output
        return tf.nn.sigmoid(y)




