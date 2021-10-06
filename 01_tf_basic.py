import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf 

# Initailization of Tensors
x = tf.constant(4, shape=(1,1), dtype=tf.float32)
y = tf.constant([[1,2,3],[4,5,6]])
ones = tf.ones((3,3))
zeros = tf.zeros((2,3))
eye = tf.eye(3)
rand_normal = tf.random.normal((3,3), mean=0, stddev=1)
print(x)
print(y)
print(ones)
print(zeros)
print(eye)
print(rand_normal)
#Mathematical Operations

#Indexing