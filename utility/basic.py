import hashlib
import subprocess
import os
from pathlib import Path

def sha(data):
    return hashlib.md5(data).hexdigest()

def open_note(data):
	# Write the content to a file.
	with open("my_file", "wb") as binary_file:
		binary_file.write(data)

	# Open the file as subprocess.
	process = subprocess.Popen(["vim", "my_file"])
	process.wait()

def read_file_contend():
	with open("my_file", "rb") as binary_file:
		return binary_file.read()

def delete_file_cache():
    temp_file = Path('my_file')  
    if temp_file.exists():
        os.remove(temp_file)
