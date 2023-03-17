import requests
import json
from threading import Thread


url = "http://10.43.12.121:5000"

def req_thread():
	# Define the URL endpoint and data to send
	
	data = {"request": "Cat-Timer:20"}

	# Convert data to JSON format
	json_data = json.dumps(data)
	# Set headers and send POST request
	headers = {'Content-type': 'application/json'}
	response = requests.post(url, data=json_data, headers=headers)

	# Print the response status code and content
	#print(response.status_code)

	resp = response.content
	print(response.content) 


timer_thread = Thread(target=req_thread)
timer_thread.start()
	
# Define the URL endpoint and data to send
url = "http://10.43.12.121:5000"
data = {"request": "Dog-Timer:10"}

# Convert data to JSON format
json_data = json.dumps(data)

# Set headers and send POST request
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

# Print the response status code and content
#print(response.status_code)

resp = response.content
print(response.content) 
