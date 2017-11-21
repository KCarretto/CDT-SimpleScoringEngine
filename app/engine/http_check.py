"""
A module for checking HTTP uptime.
"""
import requests

from enginecheck import EngineCheck

class HTTPCheck(EngineCheck):
    def __init__(self, ip_addr, points, uri):
        self.uri = uri
        EngineCheck.__init__(self, 'HTTP', ip_addr, points)
    
    def run_check(self):
        try:
            requests.get('http://{}/{}'.format(self.ip_addr, self.uri))
            return True        
        except Exception as e:
            return str(e)
