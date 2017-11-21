"""
This is the main engine module that runs checks and then sleeps after the delay.
"""
import random
import time

from threading import Thread, Event
from mongoengine import connect

from config import CHECK_DELAY, CHECK_DELTA
from config import HTTP_SERVER, HTTP_POINTS, HTTP_URI

from http_check import HTTPCheck 
from ..logger import info, debug

class Worker (Thread):
    def __init__(self, check_class, ip_addr, points, *args):
        self.ip_addr = ip_addr
        self.points = points
        self.args = args
        self.check_class = check_class
        Thread.__init__(self)
        debug("Check worker spawned for {} on {}".format(check_class.__name__, ip_addr))
    
    def run(self):
        debug("Check worker running for {} on {}".format(self.check_class.__name__, self.ip_addr))
        check = self.check_class(self.ip_addr, self.points, self.args)
        checkout = check.run_check()
        if type(checkout) != str:
            check.submit(checkout)
        else:
            check.submit(False, checkout)

class Engine(Thread):
    def __init__(self, event, tid):
        Thread.__init__(self)
        self.event = event
        self.tid = tid

    def run(self):
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

            info("All checks completed", "engine")

            delta = random.randrange(-CHECK_DELTA, CHECK_DELTA)
            time.sleep(CHECK_DELAY + delta)
