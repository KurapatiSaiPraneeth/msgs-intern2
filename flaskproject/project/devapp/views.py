#################
#### imports ####
#################
 
from flask import render_template, Blueprint

 
 
################
#### config ####
################
 
devapp_blueprint = Blueprint('devapp', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@devapp_blueprint.route('/index')
def index():
    return render_template('index.html')