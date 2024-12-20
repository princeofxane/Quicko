import getpass
import sys
import time
import internal.request as r
import utility.basic as util

running_env = 'test'

request = r.Request(env=running_env)


man = """
You can try these options:\n
Usage: 
quicko [note] [-n/-d]

List:
quicko list: lists available notes\n

Example:
quicko python -n: gets python notes\n
quicko python -d: gets python queries\n
	"""



if len(sys.argv) == 1:
	print('provde valid arguments')
	print(man)
	sys.exit()

if len(sys.argv) == 2 and sys.argv[1] == 'list':
	request.list_notes()
	sys.exit()

if len(sys.argv) == 2 and sys.argv[1] == '--help':
	print(man)
	sys.exit()


note_name = sys.argv[1]
note_flag = sys.argv[2]

note = request.get_notes(note_name, note_flag)

# Store original hash value.
old_sha = util.sha(note)

util.open_note(note)

# Check if any changes.
current_note = util.read_file_contend()
new_sha = util.sha(current_note)

# exit if no file changes.
if old_sha == new_sha:
	util.delete_file_cache()
	sys.exit()

# proceed to update if any changes.
new_content = util.read_file_contend()

# Lil wait for aesthetics. '(0_0)'
time.sleep(0.2)

print("The note has been changed\nEnter admin password")

try:
	password = getpass.getpass()
except:
	sys.exit('\nProvide a valid password!')

password_hash = util.sha(password.encode('utf-8'))

req_data = {'content':new_content, 'passHash': password_hash}

request.update_notes(note_name, note_flag, req_data)

util.delete_file_cache()
		
