from app import app
#from flask_migrate import MigrateCommand
#from flask_script import Manager


app.run(port=app.config['PORT'], debug=app.config['DEBUG'])