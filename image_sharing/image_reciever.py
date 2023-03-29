import socket
import cv2
import time

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to a specific IP address and port
host = '206.87.97.60' # replace with your server's IP address
port = 5000
s.bind((host, port))

# set the maximum number of queued connections
s.listen(5)

while True:
    # wait for a client to connect
    print('Waiting for client to connect...')
    client_socket, addr = s.accept()
    print('Got connection from', addr)

    # capture an image using the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # encode the image
    encoded, buffer = cv2.imencode('.jpg', frame)
    data = buffer.tobytes()

    # send the image size and data to the client
    size = len(data)
    header = f'{size:012d}'
    client_socket.sendall(header.encode() + data)

    # release the resources
    cap.release()
    client_socket.close()

    # wait for 5 seconds before capturing the next image
    time.sleep(5)