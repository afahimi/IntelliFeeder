from flask import Flask, request
import time
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    data = request.json
    print(data)
    if data['request'] == 'dog' or data['request'] == 'cat':
        # Forward the request to the Pico W
        # response = requests.get('http://pico-w-address/' + data['request'])
        response = "nice"
        return "amraj aujla loves kids"
    else:
        print("hello there")
        return 'Invalid request'


    """
    if data['request'] == 'dog' or data['request'] == 'cat':
        # Forward the request to the Pico W
        response = requests.get('http://pico-w-address/' + data['request'])
        return response.text
    
    """
    # elif data['request'] == 'timer':
    #     # Countdown for the timer length and then send a dog or cat request
    #     timer_length = data['length']
    #     time.sleep(timer_length)
    #     response = requests.get('http://pico-w-address/' + ['dog', 'cat'][int(time.time() % 2 == 0)])
    #     return response.text
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)