from flask import Blueprint, render_template
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from ..cmcAPI.api import Cmc
home = Blueprint('home', __name__)

@home.route('/')
def index():
    cmc = Cmc()
    all_data = cmc.get_all()
    return render_template('home/index.html', data=all_data)
"""    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url_covert, params=parameters)
        data = json.loads(response.text)
        json_string = json.dumps(data)
        with open('data.json', 'w') as outfile:
            outfile.write(json_string)
        datas = data
        print(datas)
        return render_template('home/index.html', data=data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)"""