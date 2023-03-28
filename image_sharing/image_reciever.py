import socket
import cv2

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 12345

# bind socket to a public host, and a port
s.bind((host, port))

# set the maximum number of queued connections
s.listen(5)

while True:
    # establish a connection
    client_socket, addr = s.accept()
    print('Got connection from', addr)

    # capture an image using the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # encode the image
    encoded, buffer = cv2.imencode('.jpg', frame)
    data = buffer.tobytes()

    # send the image to the client
    client_socket.sendall(data)

    # release the resources
    cap.release()
    client_socket.close()
