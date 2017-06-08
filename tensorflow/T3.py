#!-*-coding:utf-8-*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf


def t1():
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))
    sess.close()


def t2():
    a = tf.constant(2)
    b = tf.constant(3)
    with tf.Session() as sess:
        print "a=2, b=3"
        print "Addition with constants: %i" % sess.run(a + b)
        print "Multiplication with constants: %i" % sess.run(a * b)


def t3():
    a = tf.placeholder(tf.int16)
    b = tf.placeholder(tf.int16)
    add = tf.add(a, b)
    mul = tf.multiply(a, b)
    with tf.Session() as sess:
        print "Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3})
        print "Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3})


def t4():
    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant([[2.], [2.]])
    product = tf.matmul(matrix1, matrix2)
    with tf.Session() as sess:
        result = sess.run(product)
        print result


if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    t4()