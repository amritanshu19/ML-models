import tensorflow as tf
import numpy as np
from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([1.0, 0.0, 1.0, 4.0, 9.0, 16.0], dtype=float)
model.fit(xs, ys, epochs=500)
print(model.predict([5.0]))
