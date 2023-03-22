import requests
import json
import jsonify

# Define the URL endpoint and data to send
url = "http://128.189.234.234:5000"
data = {'request': 'Cat-Timer:20'}
print(data)
#data2 = {"request": "Cancel-Cat"}

# Convert data to JSON format
json_data = json.dumps(data['request'])
print(json_data)
#json_data2 = json.dumps(data2)

# Set headers and send POST request
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

for i in range(0,5):
    if i % 2 == 0:
        data = {'request': 'Left'}
    else:
        data = {'request': 'Right'}
    json_data = json.dumps(data['request'])
    response = requests.post(url, data=json_data, headers=headers)
    print(response.content)
        

# send second request
# response2 = requests.post(url, data=json_data2, headers=headers)

# Print the response status code and content
#print(response.status_code)

resp = response.content
print(response.content) 

# print(response2.content)
