"""
A module for checking if a host is pingable
"""
import subprocess

from enginecheck import EngineCheck

class ICMPCheck(EngineCheck):
    def __init__(self, params):
        ip_addr = ','.join(params['ip_addr'])
        EngineCheck.__init__(self, 'ICMP', ip_addr, params['points'])

    def run_check(self):
        try:
            for ip in self.ip_addr.split(','):
                output = subprocess.check_output("ping -c 4 {}".format(ip), shell=True)
            return True        
        except Exception as e:
            return str(e)

