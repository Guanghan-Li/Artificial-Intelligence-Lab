import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot",
]

# Load data once
(train_images, train_labels), _ = tf.keras.datasets.fashion_mnist.load_data()

# Pick the first occurrence of each class
first_idx_per_class = [np.where(train_labels == cls)[0][0] for cls in range(10)]
sample_images = train_images[first_idx_per_class]

plt.figure(figsize=(10, 2))
for i, (name, img) in enumerate(zip(CLASS_NAMES, sample_images), start=1):
    plt.subplot(1, 10, i)
    plt.imshow(img, cmap="gray")
    plt.title(name)
    plt.axis("off")

plt.tight_layout()
plt.show()
