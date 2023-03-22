from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    # Define the URL and JSON payload
    url = "http://10.43.12.121:5000/"
    payload = {"request": "Left"}

    # Convert the payload to JSON
    json_payload = json.dumps(payload)

    # Set the content type header to JSON
    headers = {"Content-Type": "application/json"}

    # Send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    # Print the response
    print(response.text)
    return response.text

if __name__ == '__main__':
    app.run(debug=True, port=5000)



# # Define the URL and JSON payload
# url = "http://10.43.12.121:5000/"
# payload = {"request": "Left"}

# # Convert the payload to JSON
# json_payload = json.dumps(payload)

# # Set the content type header to JSON
# headers = {"Content-Type": "application/json"}

# # Send the POST request with the JSON payload
# response = requests.post(url, data=json_payload, headers=headers)

# # Print the response
# print(response.text)