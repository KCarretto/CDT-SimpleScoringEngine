"""
This module serves as a basic entry point for web requests.
"""
from . import app
from flask import jsonify

@app.route('/')
def home():
    pass

@app.route('/logs')
def logs():
    pass

@app.route('/checks')
def checks():
    pass

