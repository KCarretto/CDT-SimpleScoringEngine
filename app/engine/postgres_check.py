"""
A module for checking Postgres uptime.
"""
import psycopg2

from enginecheck import EngineCheck

class PostgresCheck(EngineCheck):
    def __init__(self, params):
        self.user = params['user']
        self.password = params['password']
        self.dbname = params['dbname']
        EngineCheck.__init__(self, 'Postgres', params['ip_addr'], params['points'])
    
    def run_check(self):
        try:
            conn = psycopg2.connect("dbname = '%s' user= '%s' host = '%s' password = '%s'" % \
                    (self.dbname, self.user, self.ip_addr, self.password))
            return True        
        except Exception as e:
            return str(e)
