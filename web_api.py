#!/usr/bin/env python
from flask import Flask,jsonify
from mongo_query import mongo_query

app = Flask(__name__)

@app.route('/api/v0.1/pornhub_query',methods = ['GET','POST'])

def pornhub_query():
    return jsonify(mongo_query("N"))



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=10090)