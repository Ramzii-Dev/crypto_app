from flask import Blueprint, render_template
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from app.cmcAPI.api import Cmc
import json
import os
import app
home = Blueprint('home', __name__)

pa = os.path.abspath('.')
path_file = os.path.join(pa, 'app\\helpers\\coins.json')

@home.route('/')
def index():
     with open(path_file, 'r') as f:
        data = json.load(f)
        return render_template('home/index.html', data = data)    


