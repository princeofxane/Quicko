from ast import Param
import requests
import hashlib
import subprocess
import getpass
import os
import sys
from pathlib import Path
import time
  
try:
	note_name = sys.argv[1]
	note_flag = sys.argv[2]
except:
	sys.exit('Wrong arguments')

baseURL = "http://atrium.mountofmordor.com"
listEndpoint = "/api/v1/cs/listnote"
readEndpoint = "/api/v1/cs/readnote"
updateEndpoint = "/api/v1/cs/updatenote"

# if the note_name is list then send the list note request.
if note_name == 'list':
	r = requests.get(url = baseURL + listEndpoint)
	resp = r.json()
	note_list = resp['data']
	result = note_list.split('_')
	sorted_array = sorted(result)
	for element in sorted_array:
		print(element.capitalize())
	sys.exit()
  
# # defining a params dict for the parameters to be sent to the API
PARAMS = {'noteName':note_name, 'noteFlag': note_flag}
  
# TLS
# r = requests.get(url = URL, verify="ssl/server_ngrok.crt")

r = requests.get(url = baseURL + readEndpoint, params=PARAMS)
  
# extracting data in json format
resp = r.json()
data = resp.get('data').encode('utf-8')


# Capture the hash value of retreived data from server.
initial_hash = hashlib.md5(data).hexdigest()

 # Write the content to a file.
with open("my_file", "wb") as binary_file:
 	binary_file.write(data)

# Open the file as subprocess.
process = subprocess.Popen(["vim", "my_file"])
process.wait()

# Capture the hash after the operation.
final_hash = hashlib.md5(open('my_file','rb').read()).hexdigest()

# Proceed to update the file if there are changes.
if initial_hash != final_hash:
	with open("my_file", "rb") as binary_file:
		_content = binary_file.read()

		# A bit of a wait before message appears for aesthetics. '(0_0)'
		time.sleep(0.2)

		passInput = ""

		print("The note has been changed\n")
		print("Enter admin password")
		try:
			passInput = getpass.getpass()
		except:
			sys.exit('\nGive proper password string!')

		password_hash = hashlib.md5(passInput.encode('utf-8')).hexdigest()

		DATA = {'content':_content, 'passHash': password_hash}

		r = requests.post(url = baseURL + updateEndpoint, params=PARAMS, data=DATA)
		
		if r.json().get('status') == 200:
			print("The note has been updated.")
		else:
			print("Wrong password! Not is not updated.")
		
# Delete the caches file.
temp_file = Path('my_file')  
if temp_file.exists():
	os.remove(temp_file)
