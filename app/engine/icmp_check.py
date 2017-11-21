"""
A module for checking if a host is pingable
"""
import subprocess

from enginecheck import EngineCheck

class ICMPCheck(EngineCheck):
    def __init__(self, ip_addr, points):
        self.ip_addr = ip_addr
        EngineCheck.__init__('ICMP', ip_addr, points)

    def run_check(self):
        try:
            output = subprocess.check_output("ping -c 4 {}".format(self.ip_addr), shell=True)
            return True        
        except Exception as e:
            return str(e)

