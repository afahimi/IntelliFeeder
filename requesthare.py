from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    data = request.get_json()
    # Process the data as needed
    response_data = {'request': data}
    # Send the JSON to the specified IP address and port
    requests.post('http://192.168.137.10:5000', json=response_data)
    return jsonify({'message': 'Request forwarded'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

# host="128.189.239.223",
