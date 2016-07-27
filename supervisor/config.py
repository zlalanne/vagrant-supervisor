import json
import os
import sys

if sys.platform == 'linux':
    CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config',
                              'vagrant-supervisor')
    CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')


class Config:

    def __init__(self):
        if os.path.isfile(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                self.config = json.load(f)
            self.changes = False
        else:
            os.makedirs(CONFIG_DIR, exist_ok=True)
            self.config = {}
            self.changes = True

    def write_config(self):
        if self.changes:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.config, f)
