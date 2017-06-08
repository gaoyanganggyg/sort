import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.01
training_epochs = 2000
display_step = 50


#Training Data
train_X = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(np.random.randn())
b = tf.Variable(np.random.randn())
# activation = W * X + b
activation = tf.add(tf.multiply(X, W), b)

cost = tf.reduce_sum(tf.square(activation-Y)) / (2 * n_samples)
# cost = tf.reduce_mean(tf.square(activation - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        if epoch % display_step == 0:
            print('Epoch:%d' % (epoch+1),'cost:{:.9f}'.format(sess.run(cost,feed_dict={X:train_X,Y:train_y})),\
                  'W:',sess.run(W),'b:',sess.run(b))

    print("Optimization Finished!")
    print('Epoch:%d' % (epoch + 1), 'cost:{:.9f}'.format(sess.run(cost, feed_dict={X: train_X, Y: train_y})), \
          'W:', sess.run(W), 'b:', sess.run(b))

    plt.scatter(train_X, train_y,c='r',marker='o')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b))
    plt.show()
