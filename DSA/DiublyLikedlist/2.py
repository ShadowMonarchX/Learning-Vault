import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

# Preprocess the uploaded image
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Resize to model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize pixel values
    return img_array

# Classify the image using the loaded model
def classify_image(model, img_array):
    predictions = model.predict(img_array)
    if predictions[0][0] > predictions[0][1]:
        return 'Cat'
    else:
        return 'Dog'
