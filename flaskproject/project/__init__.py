#################
#### imports ####
#################
 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
################
#### config ####
################
 
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
 
db = SQLAlchemy(app)
 
####################
#### blueprints ####
####################
 

from project.devapp.views import devapp_blueprint
 
# register the blueprints

app.register_blueprint(devapp_blueprint)
 
