"""
A module for checking IMAP uptime.
"""
import imaplib
from enginecheck import EngineCheck

class IMAPCheck(EngineCheck):
    def __init__(self, params):
        self.user = params['user']
        self.password = params['password']
        EngineCheck.__init__(self, 'IMAP', params['ip_addr'], params['points'])
    
    def run_check(self):
        try:
            server = imaplib.IMAP4(self.ip_addr)
            server.login(self.user, self.password)
            server.select()
            typ, data = server.search(None, "ALL")
            print data
            if not data:
                raise Exception("Couldn't get messages")
            return True     
   
        except Exception as e:
            return str(e)
