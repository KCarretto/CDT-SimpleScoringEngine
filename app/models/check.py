"""
This document represents an instance of a check.

Contains:
    timestamp: The time that the check was conducted.
    check_type: The type of check conducted (i.e. SSH).
    ip_addr: The IP address of the server checked.
    points: How many points it was worth (i.e. 50).
    passed: Whether the check passed or not (True or False).abs
    status: A description of why the check failed, if it failed.
"""
from .. import db
from ..logger import *
from ..config import COLLECTION_CHECKS, MAX_FIELD_LEN

class Check(db.Document):
    meta = {
        'collection': COLLECTION_CHECKS,
    }

    start_time = db.FloatField(required=True, null=False)
    end_time = db.FloatField(required=True, null=False)
    check_type = db.StringField(required=True, null=False, max_length=MAX_FIELD_LEN)
    ip_addr = db.StringField(required=True, null=False, max_length=MAX_FIELD_LEN)
    points = db.IntField(required=True, null=False)
    passed = db.BooleanField(required=True, null=False)
    status = db.StringField(required=False, max_length=MAX_FIELD_LEN)

    def get_document(self):
        return {
            'check_type': self.check_type,
            'check_status': 'Passed' if self.passed else 'Failed' if self.status is not None else 'Frozen',
            'ip_addr': self.ip_addr,
            'points': self.points,
            'passed': self.passed,
            'status': self.status,
        }
