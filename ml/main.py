import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# Load the model
model_path = r'C:\Users\navra\OneDrive\Documents\ml\model\ssd_mobilenet_v2_320x320_coco17_tpu-8\saved_model'
model = tf.saved_model.load(model_path)
image_path = 'linares.jpg'
# Define the input and output tensors
input_tensor = model.signatures['serving_default'].inputs[0]
output_tensor = model.signatures['serving_default'].outputs[0]

# Load and preprocess the image
image = cv2.imread('linares.jpg')

# Resize the image to (1, None, None, 3)
image = cv2.resize(image, (320, 320))
image = image.reshape(1, *image.shape)

# Convert the data type to tf.uint8
image = tf.cast(image, tf.uint8)
# Make the prediction
output = model(image)
scores = output['detection_scores'][0].numpy()
classes = output['detection_classes'][0].numpy().astype(int)
boxes = output['detection_boxes'][0].numpy()

# Display the image and the predicted classes and scores
fig, ax = plt.subplots()
ax.imshow(np.array(Image.open(image_path)))
best = 0
last = ''
for i in range(len(scores)):
    if scores[i] > 0.5:
        ymin, xmin, ymax, xmax = boxes[i]
        if scores[i] > best:
            last = f'class {classes[i]}'
            best = scores[i]
        class_name = f'class {classes[i]}'

if last != '':        
    label = f'{class_name}: {best:.2f}'
    ax.add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, 
                                    edgecolor='red', facecolor='none'))
    ax.annotate(label, (xmin, ymin), color='red')
plt.show()

