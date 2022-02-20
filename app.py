#Import flask dependency
from flask import Flask

#Create new flask app instance
app = Flask(__name__)

#Create flask routes##
#Create starting point known as the root##
#@app.route('/')

#Create function called hello world after root##
#def hello_world():
    #return 'Hello world'

#Whole code:
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

