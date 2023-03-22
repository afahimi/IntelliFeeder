import requests
import json
import jsonify

# Define the URL endpoint and data to send
url = "http://127.0.0.1:5000"
data = {'request': 'Left'}
print(data)
#data2 = {"request": "Cancel-Cat"}

# Convert data to JSON format
json_data = json.dumps(data)
#json_data2 = json.dumps(data2)

# Set headers and send POST request
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

# send second request
# response2 = requests.post(url, data=json_data2, headers=headers)

# Print the response status code and content
#print(response.status_code)

resp = response.content
print(response.content) 

# print(response2.content)
