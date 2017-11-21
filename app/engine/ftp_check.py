"""
A module for checking FTP uptime.
"""
import ftplib

from enginecheck import EngineCheck

class FTPCheck(EngineCheck):
    def __init__(self, ip_addr, points, user, password):
        self.user = user
        self.password = password
        self.ip_addr = self.ip_addr
        EngineCheck.__init__('FTP', self.ip_addr, points)
    
    def run_check(self):
        try:
            server = ftplib.FTP(self.ip_addr)
            server.login(user=self.user, passwd=self.password)
            server.retrlines('LIST')
            server.quit()
            return True     
   
        except Exception as e:
            return str(e)
