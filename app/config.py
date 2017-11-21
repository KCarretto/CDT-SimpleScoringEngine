"""
A module for holding configuration settings.
"""

LOG_LEVEL = 'debug'

DB_NAME = 'scoringengine'
DB_HOST = 'localhost'
DB_PORT = 27017

MAX_FIELD_LEN = 200
MAX_LOG_LEN = 5000
COLLECTION_LOGS = 'Logs'
COLLECTION_CHECKS = 'Checks'

LOG_LEVELS = (
                'debug',
                'info',
                'warn',
                'crit',
                )