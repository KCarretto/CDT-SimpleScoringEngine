"""
A module for checking FTP uptime.
"""
import ftplib

from enginecheck import EngineCheck

class FTPCheck(EngineCheck):
    def __init__(self, params):
        self.user = params['user']
        self.password = params['password']
        EngineCheck.__init__(self, 'FTP', params['ip_addr'], params['points'])
    
    def run_check(self):
        try:
            server = ftplib.FTP(self.ip_addr, timeout=self.timeout)
            server.login(user=self.user, passwd=self.password)
            server.retrlines('LIST')
            server.quit()
            return True     
   
        except Exception as e:
            return str(e)
