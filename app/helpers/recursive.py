
import time
import json 
import os
from apscheduler.schedulers.background import BackgroundScheduler


class Recursive():
    file_path = os.path.join(os.path.dirname(__file__), 'coins.json')
    def __init__(self,day_time,data,path=file_path):
        self.day_time = day_time
        self.data = data
        self.file_path = path
        
    def start(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.func, 'interval', seconds=self.day_time)
        scheduler.start()
        

    def func(self):
        print('Hello')
        with open(self.file_path, 'w') as outfile:
            json.dump(self.data, outfile)
