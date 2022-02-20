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
def hello_world():
    return 'Hello world'

###SKILL DRILL: PRACTICE WITH SOME SAMPLE CODE TO CREATE DIFFERENT ROUTES###