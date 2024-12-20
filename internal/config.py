import yaml
import os
import getpass
import sys


def read_config():
    is_exist = False

    username = getpass.getuser()
    config_file_path = (f'/home/{username}/.config/quicko/config.yaml')

    # check if the file exist.
    if not os.path.exists(config_file_path):
        print('config file does not exist in path: ', config_file_path)
        sys.exit()

    try: 
        with open(config_file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except yaml.YAMLError as e:
        sys.exit(f'exception during reading config: {e}')

class Config:
    env = ''
    config = ''
    base_url = ''

    def __init__(self, env):

        # update the env value.
        self.env = env

        # load config file to memory.
        self.config = read_config()

        # store base url
        url = self.config[self.env]['base_url']
        if url == "":
            sys.exit('empty value for base_url')
        self.base_url = url
        
    def base_url(self):
        return self.base_url

    def read_endpoint(self):
        endpoint = self.config[self.env]['endpoints']['read']
        if endpoint == "":
            sys.exit('empty value for read endpoint')
        return self.base_url + endpoint

    def update_endpoint(self):
        endpoint = self.config[self.env]['endpoints']['update']
        if endpoint == "":
            sys.exit('empty value for update endpoint')
        return self.base_url + endpoint

    def list_endpoint(self):
        endpoint = self.config[self.env]['endpoints']['list']
        if endpoint == "":
            sys.exit('empty value list endpoint')
        return self.base_url + endpoint