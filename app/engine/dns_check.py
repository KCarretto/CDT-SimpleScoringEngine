"""
A module for checking if a domain can be resolved.
"""
import socket

from enginecheck import EngineCheck

class DNSCheck(EngineCheck):
    def __init__(self, params):
        EngineCheck.__init__(self, 'DNS', params['ip_addr'], params['points'])
    
    def run_check(self):
        try:
            socket.gethostbyname(self.ip_addr)
            return True        
        except Exception as e:
            return str(e)
