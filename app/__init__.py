import sys
import time

from flask import Flask
from flask_mongoengine import MongoEngine
from threading import Thread, Event
from mongoengine import MongoEngineConnectionError

from .config import DB_NAME, DB_HOST, DB_PORT


app = Flask(__name__)

threads = []
event = Event()
# Handle MongoDB connection first
try:
    print("Establishing database connection")
    app.config['MONGODB_SETTINGS'] = {'DB': DB_NAME, 'HOST': DB_HOST, 'PORT': DB_PORT}
    db = MongoEngine(app)
except MongoEngineConnectionError as e:
    print(e)
    print("ERROR: Could not connect to database")
    sys.exit()

from engine.engine import Engine

@app.route('/start')
def start_threads():
    for i in range(1):
        e = Engine(event=event, tid=i)
        e.start()
        threads.append(e)
    
    return 'Started'

@app.route('/stop')
def stop_threads():
    event.set()
    for t in threads:
        t.join()
    
    return 'Stopped'

from .views import *

"""
import atexit
import sys

from flask import Flask
from flask_mongoengine import MongoEngine

from mongoengine import connect, MongoEngineConnectionError

from .config import DB_NAME, DB_HOST, DB_PORT

app = Flask(__name__)

# Handle MongoDB connection first
try:
    print("Establishing database connection")
    app.config['MONGODB_SETTINGS'] = {'DB': DB_NAME, 'HOST': DB_HOST, 'PORT': DB_PORT}
    db = MongoEngine(app)
except MongoEngineConnectionError as e:
    print(e)
    print("ERROR: Could not connect to database")
    sys.exit()

from . import views

from engine.engine import Engine
t = Engine()
t.start()
t.join()
"""