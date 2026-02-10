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
        req_param = {'note_name':note_name, 'note_flag': note_flag}

        print("---------")
        print(self.config.read_endpoint())

        try:
            resp = requests.get(self.config.read_endpoint(), params=req_param)
        except Exception as e:
            sys.exit(f'request failed: {e}')

        if resp.status_code != requests.codes.ok:
            sys.exit('getnote request failed')

        json_resp = resp.json()
        data = json_resp.get('data')

        # utf-8 encoded data
        # decoded_bytes = base64.b64decode(data)
        return data.encode('utf-8')

    def update_notes(self, note_name, note_flag, data):
        req_param = {'note_name':note_name, 'note_flag': note_flag}

        try:
            resp = requests.patch(self.config.update_endpoint(), params=req_param, json=data)
        except Exception as e:
            sys.exit(f'request failed: {e}')

        if resp.status_code == requests.codes.ok:
            print("The note has been updated.")
        else:
            print("Wrong password!")

    def list_notes(self):
        try:
            resp = requests.get(self.config.list_endpoint())
        except Exception as e:
            sys.exit(f'request failed: {e}')

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