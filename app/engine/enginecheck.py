"""
A class for all scoring engine checks to inherit from.
"""
from ..models.check import Check
from ..logger import *

import time

class EngineCheck(object):
    def __init__(self, check_type, ip_addr, points):
        """
        points: The amount of points the check is worth.
        ip_addr: The ip address of the server we're checking.
        check_type: The type of check being performed (i.e. AD, DNS, SSH, etc)
        """
        self.start_time = time.time()
        self.check_type = check_type
        self.ip_addr = ip_addr
        self.points = points

        info("Running check {} on {}".format(self.check_type, self.ip_addr), "engine")

    def run_check(self):
        """
        The entry point to run the check. This should return true if the check passes,
        and a status message describing why the check failed if it didn't pass.

        Note: Use self.ip_addr to obtain the ip address of the server to check.
        """
        pass

    def submit(self, passed, status=None):
        """
        Submit the results of a check. 
        passed: True or False, whether the check suceeded or not.
        status: A message describing why the check failed. If the check passed, you may leave this as None.
        """

        c = Check(
            start_time=self.start_time,
            end_time=time.time(),
            check_type=self.check_type,
            points=self.points,
            ip_addr=self.ip_addr,
            passed=passed,
            status=status
        )
        c.save()

        info("Submitted check {} on {} | passed: {}".format(self.check_type, self.ip_addr, passed), "engine")
