import yaml

yaml_file_path = 'env.yaml'

with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)


class Config:
    env = ''
    base_url = ''
    data

    def __init__(self, env):
        # update the env value.
        self.env = env

        # load config file to memory.
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)

        # store base_url
        bUrl = data[self.env]['base_url']
        if bUrl == "":
            sys.exit('empty value for base_url')
        self.base_url = bUrl
        
    def base_url(self):
        return self.base_url

    def read_endpoint(self):
        endpoint = data[self.env]['endpoints']['read']
        if endpoint == "":
            sys.exit('empty value for read endpoint')
        return self.base_url + endpoint

    def update_endpoint(self):
        endpoint = data[self.env]['endpoints']['update']
        if endpoint == "":
            sys.exit('empty value for update endpoint')
        return self.base_url + endpoint

    def list_endpoint(self):
        endpoint = data[self.env]['endpoints']['list']
        if endpoint == "":
            sys.exit('empty value list endpoint')
        return self.base_url + endpoint