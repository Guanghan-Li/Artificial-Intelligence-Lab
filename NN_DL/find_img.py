import numpy as np
import tensorflow as tf

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
import matplotlib.pyplot as plt

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

chosen_indices = []
for cls in range(10):
    idx = np.where(train_labels == cls)[0][0]
    chosen_indices.append(idx)

plt.figure(figsize=(10, 2))
for i, idx in enumerate(chosen_indices):
    plt.subplot(1, 10, i+1)
    plt.imshow(train_images[idx].reshape(28, 28), cmap="gray")
    plt.title(class_names[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
