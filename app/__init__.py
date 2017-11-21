import sys
import time

from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import MongoEngineConnectionError

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

from .views import *
