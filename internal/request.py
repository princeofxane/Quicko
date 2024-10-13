import requests
import internal.config as cfg

class Request:
    config = ''

    def __init__(self, env):
        # quit if env is invalid.
        if env == '' or env not in ('prod', 'test'):
            quit('env value is invalid or empty')
        
        self.config = cfg.Config(env)

    def get_notes(self, note_name, note_flag):
        # constructt params
        req_param = {'noteName':note_name, 'noteFlag': note_flag}

        try:
            resp = requests.get(self.config.read_endpoint(), params=req_param)
        except:
            quit('request failed')

        resp = resp.json()
        data = resp.get('data').encode('utf-8')

        return data

    def update_notes(self, note_name, note_flag, data):
        # constructt params
        req_param = {'noteName':note_name, 'noteFlag': note_flag}
        try:
            resp = requests.post(self.config.update_endpoint(), params=req_param, data=data)
        except:
            quit('request failed') 

        if resp.json().get('status') == 200:
            print("The note has been updated.")
        else:
            print("Wrong password!")

    def list_notes(self):
        # constructt params
        try:
            resp = requests.get(self.config.list_endpoint())
        except:
            quit('request failed') 

        resp = resp.json()

        note_list = resp['data']
        result = note_list.split('_')
        sorted_array = sorted(result)
        for element in sorted_array:
            print(element.capitalize())
        quit()