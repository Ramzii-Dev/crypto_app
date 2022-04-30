from flask import Blueprint, render_template
home = Blueprint('home', __name__)
from app.helpers.json_tasks import Tasks



@home.route('/')
def index():
   data = Tasks().get_all()
   return render_template('home/index.html', data=data) 


