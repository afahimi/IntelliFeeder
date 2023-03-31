import socket
import cv2
import numpy as np
import time
import json 
import base64
import requests
import tensorflow as tf
import shutil
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specify the server's IP address and port
host = '192.168.137.58' # replace with the server's IP address
port = 5000

while True:

        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            # receive the header containing the image size
            header = s.recv(12)
            if not header:
                break
            size = int(header)

            # receive the image data
            data = b''
            while len(data) < size:
                packet = s.recv(size - len(data))
                if not packet:
                    break
                data += packet

            # decode the image data
            img = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)

            # display the image
            cv2.imwrite('Image.png', img)

            model_path = r'C:\Users\navra\OneDrive\Documents\ml\model\ssd_mobilenet_v2_320x320_coco17_tpu-8\saved_model'
            model = tf.saved_model.load(model_path)
            image_path = 'Image.png'
            # Define the input and output tensors
            input_tensor = model.signatures['serving_default'].inputs[0]
            output_tensor = model.signatures['serving_default'].outputs[0]

            # Load and preprocess the image
            image = cv2.imread('Image.png')

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
            best = 0
            for i in range(len(scores)):
                if scores[i] > 0.7:
                    if classes[i] == 1:
                        best = 1
                    elif 17 < best < 23 :
                        best = 17          
            if i == 1:
                print("Human with probability" + str(scores[i]))
            if (best == 17 or best == 1):   
                # Load image
                img = cv2.imread('Image.png')
                img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

                # Encode image as base64 string
                retval, buffer = cv2.imencode('.png', img)
                img_base64 = base64.b64encode(buffer).decode('utf-8')

                # Create JSON object
                data = {'image': img_base64}

                # Convert JSON object to string
                json_data = json.dumps(data)

                # Send JSON data to Flask server
                response = requests.post('http://cpen291-16.ece.ubc.ca/', json=json_data)
                print(response)
            print(best)

        # release the resources
            cv2.destroyAllWindows()
            s.close()


    

    # wait for 5 seconds before reconnecting
   
