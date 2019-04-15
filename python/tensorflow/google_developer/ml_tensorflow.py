import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
import tensorflow as tf

yhat = tf.constant(36,name="y_hat")
y=tf.constant(39,name="y")
loss = tf.Variable((y-yhat)**2,name="loss")
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(loss))