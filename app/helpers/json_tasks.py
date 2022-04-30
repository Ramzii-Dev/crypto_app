import os
import json

path_file = os.path.join(os.path.abspath('.'), 'app\\helpers\\coins.json')

class Tasks:
    def __init__(self, ):
        with open(path_file,'r') as f:
            self.tasks = json.load(f)
    def get_by_name(self, name):
        for task in self.tasks:
            if task['name'] == name:
                return task
    def get_all(self):
        return self.tasks

