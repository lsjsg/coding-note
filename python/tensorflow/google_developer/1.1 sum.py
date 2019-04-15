from __future__ import print_function
import tensorflow as tf


g = tf.Graph()
with g.as_default():
    x = tf.constant(8,name = "x_const")
    y = tf.constant(5,name = "y_const")
    z = tf.constant(4,name = "z_const")
    tmp = tf.add(x,y,name="x_y_tmp")
    sum = tf.add(tmp,z,name="z_tmp_sum")


with tf.Session() as sess:
    print(sum.eval())