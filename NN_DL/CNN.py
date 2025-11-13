from tensorflow import keras
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))
train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()
#2
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same', strides = (1,1), input_shape=(28, 28, 1)))
#3
model.add(layers.MaxPooling2D((2, 2), padding='same', strides = (2,2)))
#4
model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same', strides = (1,1)))
#5
model.add(layers.MaxPooling2D((2, 2), padding='same', strides = (2,2)))
#6
model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same', strides = (1,1)))
#7
model.add(layers.Flatten())
#8
model.add(layers.Dense(64, 
    activation='relu')
    )
#9
model.add(layers.Dense(10, 
    activation='softmax')
    )

model.compile(
    optimizer='adam', 
    loss='sparse_categorical_crossentropy', 
    metrics=['accuracy']
    )

model.fit(train_images, train_labels, 
    epochs=5, 
    batch_size=32, 
    validation_data=(test_images, test_labels)
    )

# Predict labels for test set
y_pred_cnn = np.argmax(model.predict(test_images), axis=1)

# Calculate test set accuracy
test_acc_cnn = np.mean(y_pred_cnn == test_labels)
print("Problem 2 Test Accuracy:", test_acc_cnn)

# If you don't have this already from earlier, define the class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Show confusion matrix
cm_cnn = confusion_matrix(test_labels, y_pred_cnn)
disp_cnn = ConfusionMatrixDisplay(confusion_matrix=cm_cnn, display_labels=class_names)
disp_cnn.plot(cmap=plt.cm.Blues, xticks_rotation=45)
plt.title("Confusion Matrix (Problem 2: CNN)")
plt.show()