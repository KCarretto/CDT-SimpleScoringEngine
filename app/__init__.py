import sys

from flask import Flask
from flask_mongoengine import MongoEngine

from mongoengine import connect, MongoEngineConnectionError

from .config import DB_NAME, DB_HOST, DB_PORT
from .logger import *

app = Flask(__name__)

try:
    app.config['MONGODB_SETTINGS'] = {'DB': DB_NAME, 'HOST': DB_HOST, 'PORT': DB_PORT}
    db = MongoEngine(app)
except MongoEngineConnectionError as e:
    crit("Could not connect to database", "database")
    debug("Database connection error: {}".format(e), "database")
    sys.exit("Could not connect to database.")


from . import views