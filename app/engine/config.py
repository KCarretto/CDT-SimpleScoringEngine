"""
This module contains settings for the engine configuration.
"""

# Engine Settings
CHECK_DELAY = 60
CHECK_DELTA = 20
CHECK_TIMEOUT = 5

# HTTP Check Settings
HTTP_SERVER = '123.232.232.21'
HTTP_POINTS = 50
HTTP_URI = ''

# DNS Check Settings
DNS_SERVER = 'google.com'
DNS_POINTS = 50

# SSH Check Settings
SSH_SERVERS = [DNS_SERVER, HTTP_SERVER]
SSH_POINTS = 50
SSH_USER = 'root'
SSH_PASSWORD = 'changeme'

# FTP Check Settings
FTP_SERVER = '8.8.8.8'
FTP_POINTS = 50
FTP_USER = 'root'
FTP_PASSWORD = 'changeme'

# SMTP Check Settings
SMTP_SERVER = '8.8.8.8'
SMTP_POINTS = 50
SMTP_USER = 50
SMTP_PASSWORD = 'changeme'


# LDAP Check Settings
LDAP_SERVER = '8.8.8.8'
LDAP_POINTS = 50
LDAP_USER ='administrator'
LDAP_PASSWORD = 'changeme'
LDAP_BASEDN = ''
LDAP_USERDN = ''

# ICMP Check Settings
ICMP_SERVERS = [HTTP_SERVER, DNS_SERVER]
ICMP_POINTS = 10

# Postgres Settings
PG_SERVERS = ''
PG_POINTS = 50
PG_DB = 'chuckecheeses'
PG_USER = 'admin'
PG_PASSWORD = 'password'
