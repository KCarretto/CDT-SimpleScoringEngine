"""
This document represents a log message from either the engine, or web application.

Contains:
    timestamp: The time the log message was generated.
    application: Whether the log was from the engine or from the web application.
    level: The log level (i.e. debug)
    message: The log message.
"""
from .. import db
from ..config import COLLECTION_LOGS, MAX_FIELD_LEN, MAX_LOG_LEN, LOG_LEVELS

class Log(db.Document):
    meta = {
            'collection': COLLECTION_LOGS,      
        }

    timestamp = db.FloatField(required=True, null=False)
    application = db.StringField(required=True,null=False, max_length=MAX_FIELD_LEN)
    level = db.StringField(required=True, null=False, max_length=MAX_FIELD_LEN, choices=LOG_LEVELS)
    message = db.StringField(required=True, null=False, max_length=MAX_LOG_LEN)

    def get_document(self):
        return {
            "timestamp": self.timestamp,
            "application": self.application,
            "level": self.level,
            "message": self.message,
        }