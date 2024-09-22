import yaml
import os
import sys

    
def get_resource_path(relative_path):
    # This will resolve the path whether you are 
    # running as a bundled executable or a script
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



def open_file():
    yaml_file_path = get_resource_path('config/env.yaml')

    # Check if the file exist
    if os.path.isfile(yaml_file_path):
        with open(yaml_file_path, 'r') as file:
            data = file.read()
    else:
        sys.exit(f"File not found: {yaml_file_path}")

    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data
    


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