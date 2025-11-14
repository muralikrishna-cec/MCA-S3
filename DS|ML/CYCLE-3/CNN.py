# FOR MODULE ERROR; ADD NEW CELL -> TYPE AND RUN:- pip install tensorflow
import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models
import matplotlib.pyplot as plt
# Load and normalize the CIFAR-10 dataset
(train_images, train_labels), (test_images, test_labels) =datasets.cifar10.load_data()
train_images, test_images = train_images / 255.0, test_images /255.0
# Class names for CIFAR-10
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship', 'truck']
# Plotting the first 25 images from the training set
plt.figure(figsize=(10, 10))
for i in range(25):
 plt.subplot(5, 5, i + 1)
 plt.xticks([])
 plt.yticks([])
 plt.grid(False)
 plt.imshow(train_images[i])
 plt.xlabel(class_names[train_labels[i][0]])
 
plt.show()
# Building the CNN model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',
input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# Adding Dense layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))
print("Architecture of the model:\n")
model.summary()
# Compiling the model
model.compile(optimizer='adam',
loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
# Training the model
history = model.fit(train_images, train_labels, epochs=10,validation_data=(test_images, test_labels))
# Evaluating the model
test_loss, test_acc = model.evaluate(test_images, test_labels,verbose=2)
print("Test loss:", test_loss)
print("Test accuracy:", test_acc)

# Plotting training and validation accuracy/loss
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()