import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import os
import certifi

# Set SSL certificate path
os.environ['SSL_CERT_FILE'] = certifi.where()

# Load pre-trained MobileNetV2 model + higher level layers
weights_path = os.path.join(os.getcwd(), 'mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5')
model = MobileNetV2(weights=weights_path)

def preprocess_image(img_path):
    img = Image.open(img_path)
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

def predict_image(img_path):
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0][0]
    return decoded_predictions

if __name__ == "__main__":
    img_path = input("Enter the path to the image: ")
    prediction = predict_image(img_path)
    label, confidence = prediction[1], prediction[2]
    print(f"Predicted: {label} with confidence: {confidence:.2f}")
