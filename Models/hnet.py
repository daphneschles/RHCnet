import numpy as np

import sys
import os
import warnings

import tensorflow as tf
from tensorflow import math as tfm
import tensorflow.keras.backend as K
sys.path.append('..')


# set the random seed
SEED_VALUE = 780255
os.environ['PYTHONHASHSEED']=str(SEED_VALUE)
tf.random.set_seed(SEED_VALUE)

'''
Append additional dense layers to a given pre-trained set of layers
'''
class AppendNet(tf.keras.Model) :
    def __init__(self, 
        pretrained_model, 
        new_layers = [64,48,24,4], 
        dout_rate = 0.5,
        act_f = tf.nn.relu) :

        super(AppendNet, self).__init__()

        self.pretrained_model = pretrained_model
        self.act_f = act_f

        self.dense_layers = []
        self.dropout_layers = []

        for d in new_layers[:-1] :
            self.dense_layers.append(tf.keras.layers.Dense(d))
            self.dropout_layers.append(tf.keras.layers.Dropout(dout_rate, seed=SEED_VALUE))
            
        self.final_layer = tf.keras.layers.Dense(new_layers[-1])


    def call(self, x, training=False, tr=None) :
        
        if tr != None:
            warnings.warn(
                "WARNING: argument 'tr' is deprecated and will be removed in the future."
            )
                  
                  
        y = self.pretrained_model(x)

        for i in range(len(self.dense_layers)) :
            y = self.act_f(y)
            y = self.dense_layers[i](y)
            y = self.dropout_layers[i](y, training=training)
        y = self.final_layer(y)

        # sigmoid activation function on output
        return tf.nn.sigmoid(y)


# a series of functions that we need to load the pre-trained model
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

def simclr_loss(_, hidden):
    """https://arxiv.org/abs/2002.05709"""
    temperature = .1
    large_num = 1e9
    hidden = tf.math.l2_normalize(hidden, -1)
    hidden1, hidden2 = tf.split(hidden, 2, 0)  
    batch_size = tf.shape(hidden1)[0]
    labels = tf.one_hot(tf.range(batch_size), batch_size * 2)
    masks = tf.one_hot(tf.range(batch_size), batch_size)  # masks diagonals, aka self similarities
    logits_aa = tf.matmul(hidden1, hidden1, transpose_b=True) / temperature
    logits_aa = logits_aa - masks * large_num
    logits_bb = tf.matmul(hidden2, hidden2, transpose_b=True) / temperature
    logits_bb = logits_bb - masks * large_num
    logits_ab = tf.matmul(hidden1, hidden2, transpose_b=True) / temperature
    logits_ba = tf.matmul(hidden2, hidden1, transpose_b=True) / temperature
    loss_a = tf.compat.v1.losses.softmax_cross_entropy(
        labels, tf.concat([logits_ab, logits_aa], 1),
    )
    loss_b = tf.compat.v1.losses.softmax_cross_entropy(
        labels, tf.concat([logits_ba, logits_bb], 1),
    )
    return loss_a + loss_b


def simclr_accuracy(_, hidden):
    hidden = tf.math.l2_normalize(hidden, -1)
    large_num = 1e9
    hidden1, hidden2 = tf.split(hidden, 2, 0)  
    batch_size = tf.shape(hidden1)[0]
    labels = tf.one_hot(tf.range(batch_size), batch_size * 2)
    masks = tf.one_hot(tf.range(batch_size), batch_size)  # masks diagonals, aka self similarities
    logits_aa = tf.matmul(hidden1, hidden1, transpose_b=True)
    logits_aa = logits_aa - masks * large_num
    logits_bb = tf.matmul(hidden2, hidden2, transpose_b=True)
    logits_bb = logits_bb - masks * large_num
    logits_ab = tf.matmul(hidden1, hidden2, transpose_b=True)
    logits_ba = tf.matmul(hidden2, hidden1, transpose_b=True)
    loss_a = tf.keras.metrics.categorical_accuracy(
        labels, tf.concat([logits_ab, logits_aa], 1),
    )
    loss_b = tf.keras.metrics.categorical_accuracy(
        labels, tf.concat([logits_ba, logits_bb], 1),
    )
    return tf.add(tf.reduce_mean(loss_a), tf.reduce_mean(loss_b)) / 2
