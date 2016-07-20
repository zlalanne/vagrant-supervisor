import json


class Config(object):

    def __init__(self):
        with open('config.json', 'r') as f:
            self.config = json.load(f)

    def write_config(self):
        with open('config.json', 'w') as f:
            json.dump(self.config, f)
