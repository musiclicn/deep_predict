import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

# Generate dummy data
import numpy as np
category = 2

x_raw = np.load(r'C:\Users\cheng\dev\data\features.npy')
y_raw = np.load(r'C:\Users\cheng\dev\data\label.npy')

print(x_raw.shape)
train_size = 1500

x_train = x_raw[:train_size]
y_train = keras.utils.to_categorical(y_raw[:train_size], num_classes=category)
print(x_train.shape)
x_test = x_raw[train_size:]
y_test = keras.utils.to_categorical(y_raw[train_size:], num_classes=category)
print(x_test.shape)

# x_train = np.random.random((1000, 20))
# y_train = keras.utils.to_categorical(np.random.randint(category, size=(1000, 1)), num_classes=category)
# x_test = np.random.random((100, 20))
# y_test = keras.utils.to_categorical(np.random.randint(category, size=(100, 1)), num_classes=category)

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(64, activation='relu', input_dim=26))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(category, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)

print('evaluation result:')
score = model.evaluate(x_test, y_test, batch_size=128)
print(model.metrics_names)
print(score)