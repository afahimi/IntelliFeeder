import requests
import json
from threading import Thread
import time

url = "http://192.168.137.10:5000"

def req_thread():
	# Define the URL endpoint and data to send
	
	data = {"request": "Left"}

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
time.sleep(2)
# Define the URL endpoint and data to send
url = "http://192.168.137.10:5000"
data = {"request": "Cancel-Dog"}

	# Convert data to JSON format
json_data = json.dumps(data)
	# Set headers and send POST request
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

	# Print the response status code and content
print(response.status_code)

resp = response.content
print(response.content) 
