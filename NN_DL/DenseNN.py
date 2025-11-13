import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train = x_train.reshape(-1, 28 * 28)
x_test = x_test.reshape(-1, 28 * 28)

model = keras.Sequential([
    keras.layers.Input(shape=(784,)),             
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))

# Predict labels for test set
y_pred_dense = np.argmax(model.predict(x_test), axis=1)

# Calculate test set accuracy
test_acc_dense = np.mean(y_pred_dense == y_test)
print("Problem 1 Test Accuracy:", test_acc_dense)

# If you don't have this already from earlier, define the class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Show confusion matrix
cm_dense = confusion_matrix(y_test, y_pred_dense)
disp_dense = ConfusionMatrixDisplay(confusion_matrix=cm_dense, display_labels=class_names)
disp_dense.plot(cmap=plt.cm.Blues, xticks_rotation=45)
plt.title("Confusion Matrix (Problem 1: Dense NN)")
plt.show()