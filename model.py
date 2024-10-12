# model.py
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Function to load pre-trained MobileNetV2 model
def load_model():
    model = MobileNetV2(weights='imagenet')
    return model

# Function to classify the uploaded image
def classify_image(model, img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    return decode_predictions(preds, top=3)[0]
