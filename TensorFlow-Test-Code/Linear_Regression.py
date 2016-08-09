
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


num_points = 1000
vectors_set = []
for i in xrange(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])


x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

## Computational Graph Designing ##
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b
loss = tf.reduce_mean(tf.square(y - y_data))

# Optimization Operation Definition
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.initialize_all_variables()
## TensorFlow Graph Designing

# We instantiate a vehicle
sess = tf.Session()
sess.run(init)


