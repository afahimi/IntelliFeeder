import requests
import json

# Define the URL endpoint and data to send
url = "http://localhost:5000"
data = {"request": "dog"}

# Convert data to JSON format
json_data = json.dumps(data)

# Set headers and send POST request
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

# Print the response status code and content
#print(response.status_code)

resp = response.content
resp2 = resp.split(\')
print(response.content) 
