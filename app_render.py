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
    try:
        name = request.args.get('name')
        assert name
    except:
        name = 'lame'
    return render_template('tutorial.html', name=name)

if __name__ == "__main__":
    app.run()