"""
A module for checking HTTP uptime.
"""
import requests

from enginecheck import EngineCheck

class HTTPCheck(EngineCheck):
    def __init__(self, params):
        self.uri = params['uri']
        EngineCheck.__init__(self, 'HTTP', params['ip_addr'], params['points'])
    
    def run_check(self):
        try:
            requests.get('http://{}/{}'.format(self.ip_addr, self.uri))
            return True        
        except Exception as e:
            return str(e)
