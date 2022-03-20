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

@app.route('/')
def hello_world():
    return 'Hello Booboo !'



@app.route("/user")
def users():
    my_user = os.environ['user']
    msg = "user: " + my_user
    return msg

@app.route("/mongo_data")
def mongo_data():
    
    
    my_pass = os.environ['pass']
    user_name = os.environ['user']
    connection_string = "mongodb+srv://" + user_name + ":" + my_pass + "@project1.q26cg.mongodb.net/project1?retryWrites=true&w=majority"


    try:
        client = MongoClient(connection_string)
        db = client.project1
        collection = db.project1
        query_mongo_df  = pd.DataFrame(list(collection.find()))
        first_20 = query_mongo_df.head(20)
    except Exception as e:
        return("error" + str(e))
    return first_20.to_html()
    

@app.route("/pass")
def passes():
    my_pass = os.environ['pass']
    msg = "pass: " + my_pass
    return msg

@app.route("/vars")
def vars():
    my_vars = os.environ
    my_vars_dict = dict(my_vars)
    return jsonify(my_vars_dict)


@app.route("/random")
def random():
    
    ret_val = "your random number is: " + str(randrange(100))
    return ret_val

if __name__ == '__main__':
    app.run()