import requests
import sys
import internal.config as cfg
import base64
import json
import http

class Request:
    config = ''

    def __init__(self, env):
        # quit if env is invalid.
        if env == '' or env not in ('prod', 'test'):
            sys.exit('env value is invalid or empty')
        
        self.config = cfg.Config(env)

    def get_notes(self, note_name, note_flag):
        # constructt params
        req_param = {'noteName':note_name, 'noteFlag': note_flag}

        try:
            resp = requests.get(self.config.read_endpoint(), params=req_param)
        except:
            sys.exit('request failed')

        if resp.status_code != requests.codes.ok:
            sys.exit('getnote request failed')

        json_resp = resp.json()
        data = json_resp.get('data')

        # utf-8 encoded data
        decoded_bytes = base64.b64decode(data)

        return decoded_bytes

    def update_notes(self, note_name, note_flag, data):
        req_param = {'noteName':note_name, 'noteFlag': note_flag}
        try:
            resp = requests.post(self.config.update_endpoint(), params=req_param, data=data)
        except:
            sys.exit('request failed') 

        if resp.status_code == requests.codes.ok:
            print("The note has been updated.")
        else:
            print("Wrong password!")

    def list_notes(self):
        try:
            resp = requests.get(self.config.list_endpoint())
        except:
            sys.exit('request failed') 
        
        if resp.status_code != requests.codes.ok:
            sys.exit('getlist request failed')

        json_resp = resp.json()

        data = json_resp.get('data')

        result = data.split('_')
        sorted_array = sorted(result)
        
        print('available notes....\n')
        for index, element in enumerate(sorted_array):
            print(f'{index + 1}. {element.capitalize()}')
        sys.exit()