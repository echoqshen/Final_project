from flask import Flask
from flask import jsonify
import pandas as pd
import random
import os
from random import randrange
from pymongo import MongoClient
from flask import render_template
app = Flask(__name__)


@app.route('/graph')
def grapher():
    return render_template('Event_Impact.html')

if __name__ == '__main__':
   app.run()
