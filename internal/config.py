import yaml
import os
import sys


def get_config_path():
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running as normal script
        base_path = os.path.dirname(os.path.abspath(__file__))
        # go up one level since config.py is in internal/
        base_path = os.path.dirname(base_path)

    return os.path.join(base_path, 'config', 'config.yaml')


def read_config():
    config_file_path = get_config_path()

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
        self.env = env
        self.config = read_config()

        url = self.config[self.env]['base_url']
        if url == "":
            sys.exit('empty value for base_url')
        self.base_url = url
    
    def create_endpoint(self):
        endpoint = self.config[self.env]['endpoints']['create']
        if endpoint == "":
            sys.exit('empty value for create endpoint')
        return self.base_url + endpoint

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