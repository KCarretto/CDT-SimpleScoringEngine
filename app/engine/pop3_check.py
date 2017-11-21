"""
A module for checking POP3 uptime.
"""
import poplib
from enginecheck import EngineCheck

class POP3Check(EngineCheck):
    def __init__(self, params):
        self.user = params['user']
        self.password = params['password']
        EngineCheck.__init__(self, 'POP3', params['ip_addr'], params['points'])
    
    def run_check(self):
        try:
            server = poplib.POP3(self.ip_addr)
            server.user = self.user
            server.pass_ = self.password
            num_messages = server.stat()
            if not num_messages:
                raise Exception("Couldn't list mailbox")
            return True     
   
        except Exception as e:
            return str(e)
