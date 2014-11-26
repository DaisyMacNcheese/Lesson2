#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        name = request.args.get('name')
        assert name
    except:
        name = 'lame'
    return "Hello %s" % str(name)

@app.route("/render")
def render():
    req_headers = request.headers

    try:
        name = request.args.get('name')
        assert name
    except:
        name = 'lame'
    return render_template('tutorial2.html',
                           name=name,
                           headers=req_headers)

if __name__ == "__main__":
    app.run()