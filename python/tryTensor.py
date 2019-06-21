"""
Try building a Neural Network with tensorFlow package.
not yet in use.
"""

from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.contrib.layers import InputLayer

print(tf.__version__)

def build_cnn(input_var=None):
    l_in = InputLayer(shape=(None, 1, 64, 512), input_var=input_var)

    l_conv1 = Conv2DLayer(incoming = l_in, num_filters = 32, filter_size = (1, 3),
                        stride = 1, pad = 'same', W = lasagne.init.Normal(std = 0.02),
                        nonlinearity = lasagne.nonlinearities.rectify)

    l_pool1 = Pool2DLayer(incoming = l_conv1, pool_size = (1, 2), stride = (2, 2))

    l_fc = lasagne.layers.DenseLayer(
            lasagne.layers.dropout(l_pool1, p=.5),
            num_units=256,
            nonlinearity=lasagne.nonlinearities.rectify)

    l_out = lasagne.layers.DenseLayer(
            lasagne.layers.dropout(l_fc, p=.5),
            num_units=2,
            nonlinearity=lasagne.nonlinearities.softmax)

    return l_out

def iterate_minibatches(inputs, targets, batchsize, shuffle=False):
    assert len(inputs) == len(targets)
    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batchsize + 1, batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield inputs[excerpt], targets[excerpt]

def main(model='cnn', batch_size=500, num_epochs=500):
    input_var = T.tensor4('inputs')
    target_var = T.ivector('targets')

    network = build_cnn(input_var)

    prediction = lasagne.layers.get_output(network)
    loss = lasagne.objectives.categorical_crossentropy(prediction, target_var)
    loss = loss.mean()

    train_acc = T.mean(T.eq(T.argmax(prediction, axis=1), target_var),dtype=theano.config.floatX)

    params = lasagne.layers.get_all_params(network, trainable=True)

    updates = lasagne.updates.nesterov_momentum(loss, params, learning_rate=0.01)

    test_prediction = lasagne.layers.get_output(network, deterministic=True)
    test_loss = lasagne.objectives.categorical_crossentropy(test_prediction,target_var)
    test_loss = test_loss.mean()

    test_acc = T.mean(T.eq(T.argmax(test_prediction, axis=1), target_var),dtype=theano.config.floatX)

    train_fn = theano.function([input_var, target_var], [loss, train_acc], updates=updates)

    val_fn = theano.function([input_var, target_var], [test_loss, test_acc])

    print("Starting training...")

    for epoch in range(num_epochs):
        # full pass over the training data:
        train_err = 0
        train_acc = 0
        train_batches = 0
        start_time = time.time()
        for batch in iterate_minibatches(train_data, train_labels, batch_size, shuffle=True):
            inputs, targets = batch
            err, acc = train_fn(inputs, targets)
            train_err += err
            train_acc += acc
            train_batches += 1

        # full pass over the validation data:
        val_err = 0
        val_acc = 0
        val_batches = 0
        for batch in iterate_minibatches(val_data, val_labels, batch_size, shuffle=False):
            inputs, targets = batch
            err, acc = val_fn(inputs, targets)
            val_err += err
            val_acc += acc
            val_batches += 1

    # After training, compute the test predictions/error:
    test_err = 0
    test_acc = 0
    test_batches = 0
    for batch in iterate_minibatches(test_data, test_labels, batch_size, shuffle=False):
        inputs, targets = batch
        err, acc = val_fn(inputs, targets)
        test_err += err
        test_acc += acc
        test_batches += 1

# Run the model
main(batch_size=5, num_epochs=30)