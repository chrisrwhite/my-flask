# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:39:20 2016

@author: Chris
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()