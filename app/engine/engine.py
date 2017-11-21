"""
This is the main engine module that runs checks and then sleeps after the delay.
"""
import random
import threading
import time

from config import CHECK_DELAY, CHECK_DELTA
from config import HTTP_SERVER, HTTP_POINTS, HTTP_URI

from http_check import HTTPCheck 
from ..logger import info

class Worker (threading.Thread):
    def __init__(self, check_class, ip_addr, points, *args):
        self.ip_addr = ip_addr
        self.points = points
        self.args = args
        self.check_class = check_class
        threading.Thread.__init__(self)
    
    def run(self):
        check = self.check_class(self.ip_addr, self.points, self.args)
        check.run_check()

class Engine(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run (self):
        if CHECK_DELAY <= CHECK_DELTA:
            print("ERROR: CHECK_DELAY must be greater than CHECK_DELTA")

        while True:
            threads = []

            # HTTP Check Thread
            info("Spawning HTTP check worker", "engine")
            httpCheck = Worker(HTTPCheck, HTTP_SERVER, HTTP_POINTS, HTTP_URI)
            httpCheck.start()
            threads.append(httpCheck)

            # Wait for checks to complete
            for t in threads:
                t.join()

            delta = random.randrange(-CHECK_DELTA, CHECK_DELTA)
            time.sleep(CHECK_DELAY + delta)