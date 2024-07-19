from ast import Param
import requests
import grpc
import hashlib
import subprocess
import getpass
import gdown
import os
import sys
from pathlib import Path
import time
  

# Handle arguments.
try:
	note_name = sys.argv[1]
	note_flag = sys.argv[2]
except:
	sys.exit('Wrong arguments')

# Clear certifcate.
if note_name == 'clear' and note_flag == '-c':
	cert_file = Path('cs_server.crt')  
	if cert_file.exists():
		os.remove(cert_file)
		sys.exit('file removed')
		
	else:
		sys.exit('file dont exist')
	
# api-endpoint
# baseURL = "http://raspberrypi.lan:8000"
baseURL = "http://atrium.mountofmordor.com"
# baseURL = "http://7b9c-103-252-25-63.ngrok.io"
readURL = baseURL + "/api/v1/cs/readnote"
updateURL = baseURL + "/api/v1/cs/updatenote"
# readURL = "http://localhost:8000/api/v1/cs/readnote"
# updateURL = "http://localhost:8000/api/v1/cs/updatenote"
  
# # defining a params dict for the parameters to be sent to the API
PARAMS = {'noteName':note_name, 'noteFlag': note_flag}
  
# TLS
# r = requests.get(url = URL, verify="ssl/server_ngrok.crt")

r = requests.get(url = readURL, params=PARAMS)
  
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
		print("Enter admin pasimport requests")
		try:
			passInput = getpass.getpass()
		except:
			sys.exit('\nGive proper password string!')

		password_hash = hashlib.md5(passInput.encode('utf-8')).hexdigest()

		DATA = {'content':_content, 'passHash': password_hash}

		r = requests.post(url = updateURL, params=PARAMS, data=DATA)
		
		if r.json().get('status') == 200:
			print("The note has been updated.")
		else:
			print("Wrong password! Not is not updated.")
		
# Delete the caches file.
temp_file = Path('my_file')  
if temp_file.exists():
	os.remove(temp_file)