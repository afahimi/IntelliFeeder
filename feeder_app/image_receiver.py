import socket
import cv2
import numpy as np
import time

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specify the server's IP address and port
host = '206.12.64.192' # replace with the server's IP address
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

        # release the resources
            cv2.destroyAllWindows()
            s.close()
            time.sleep(5)




    # wait for 5 seconds before reconnecting
