#!-*-coding:utf-8-*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

learnig_rate = 0.01
training_epochs = 2000
display_steps = 50


def t1():
    train_X = np.asarray(
        [3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167, 7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1])
    train_Y = np.asarray(
        [1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221, 2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3])
    n_samples = train_X.shape[0]
    X = tf.placeholder('float')
    Y = tf.placeholder('float')

    W = tf.Variable(np.random.rand(), name='weight')
    b = tf.Variable(np.random.rand(), name='bias')

    activation = tf.add(tf.multiply(X, W), b)

    cost = tf.reduce_sum(tf.pow(activation-Y, 2)/(2*n_samples))
    optimizer = tf.train.GradientDescentOptimizer(learnig_rate).minimize(cost)

    init = tf.initialize_all_variables()

    with tf.Session() as sess:
        sess.run(init)

        for epoch in range(training_epochs):
            for (x, y) in zip(train_X, train_Y):
                sess.run(optimizer, feed_dict={X: x, Y: y})

            if epoch % display_steps == 0:
                print("Epoch:", '%04d' % (epoch+1), "cost=",
                      "{:.9f}".format(sess.run(cost, feed_dict={X: train_X, Y: train_Y})),
                      "W=", sess.run(W), "b=", sess.run(b))
        print("Optimization Finished!")
        print("cost=", sess.run(cost, feed_dict={X: train_X, Y: train_Y}),
                "W=", sess.run(W), "b=", sess.run(b))

        plt.plot(train_X, train_Y, 'ro', label='Original data')
        plt.plot(train_X, sess.run(W)*train_X+sess.run(b), label='Fitted line')

        plt.legend()
        plt.show()

if __name__ == '__main__':
    t1()