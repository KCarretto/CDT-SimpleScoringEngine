"""
A module for checking if a domain can be resolved.
"""
import socket

from enginecheck import EngineCheck

class DNSCheck(EngineCheck):
    def __init__(self, ip_addr, points):
        self.ip_addr = ip_addr
        EngineCheck.__init__('DNS', ip_addr, points)
    
    def run_check(self):
        try:
            socket.gethostbyname("chucke.cheese")
            return True        
        except Exception as e:
            return str(e)
