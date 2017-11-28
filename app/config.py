"""
A module for holding configuration settings.
"""

# Log Settings
LOG_LEVEL = 'debug'
LOG_LEVELS = (
                'debug',
                'info',
                'warn',
                'crit',
            )

# Database Connection
DB_NAME = 'scoringengine'
DB_HOST = 'localhost'
DB_PORT = 27017

# Document Settings
MAX_FIELD_LEN = 5000
MAX_LOG_LEN = 5000
MAX_RESULTS = 500

# Collection Settings
COLLECTION_LOGS = 'Logs'
COLLECTION_CHECKS = 'Checks'

# Scoreboard Settings
SCORED_CHECKS = [
    'LDAP',
    'DNS',
    'HTTP',
    'SSH',
    'FTP',
    'SMTP',
    'ICMP',
    'Postgres',
]


