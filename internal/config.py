import yaml
import os
import getpass
import sys


# default_config is the config that gets loaded if config file not provided.
default_config = {
    'prod': {
        'base_url': 'http://atrium.mountofmordor.com',
        'endpoints': {
            'read': '/api/v1/cs/readnote',
            'update': '/api/v1/cs/updatenote',
            'list': '/api/v1/cs/listnote'
        }
    },
    'test': {
        'base_url': 'http://localhost:8080'
    }
}
    

def open_file():
    is_exist = False

    username = getpass.getuser()
    config_file_path = (f'/home/{username}/.config/quicko/config.yaml')

    # check if the file exist.
    if os.path.exists(config_file_path):
        is_exist = True

    if is_exist:
        try: 
            with open(config_file_path, 'r') as file:
                data = yaml.safe_load(file)
                return data
        except yaml.YAMLError as e:
            sys.exit(f'some execption occured: {e}')
            
    return default_config
    
    


class Config:
    env = ''
    data = ''
    base_url = ''

    def __init__(self, env):

        # update the env value.
        self.env = env

        # load config file to memory.
        self.data = open_file()

        # store base_url
        bUrl = self.data[self.env]['base_url']
        if bUrl == "":
            sys.exit('empty value for base_url')
        self.base_url = bUrl
        
    def base_url(self):
        return self.base_url

    def read_endpoint(self):
        endpoint = self.data[self.env]['endpoints']['read']
        if endpoint == "":
            sys.exit('empty value for read endpoint')
        return self.base_url + endpoint

    def update_endpoint(self):
        endpoint = self.data[self.env]['endpoints']['update']
        if endpoint == "":
            sys.exit('empty value for update endpoint')
        return self.base_url + endpoint

    def list_endpoint(self):
        endpoint = self.data[self.env]['endpoints']['list']
        if endpoint == "":
            sys.exit('empty value list endpoint')
        return self.base_url + endpoint