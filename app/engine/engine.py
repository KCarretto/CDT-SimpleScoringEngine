"""
This is the main engine module that runs checks and then sleeps after the delay.
"""
import random
import time

from ..logger import info, debug

from threading import Thread, Event
from mongoengine import connect

from config import CHECK_DELAY, CHECK_DELTA
from config import HTTP_SERVER, HTTP_POINTS, HTTP_URI
from config import DNS_SERVER, DNS_POINTS
from config import SSH_SERVERS, SSH_POINTS, SSH_USER, SSH_PASSWORD
from config import FTP_SERVER, FTP_POINTS, FTP_USER, FTP_PASSWORD
from config import ICMP_SERVERS, ICMP_POINTS

from http_check import HTTPCheck 
from dns_check import DNSCheck
from ssh_check import SSHCheck
from ftp_check import FTPCheck
from icmp_check import ICMPCheck

class Worker (Thread):
    def __init__(self, check_class, ip_addr, points, **kwargs):
        self.ip_addr = ip_addr
        self.points = points
        self.kwargs = kwargs
        self.check_class = check_class
        Thread.__init__(self)
        debug("Check worker spawned for {} on {}".format(check_class.__name__, ip_addr))
    
    def run(self):
        debug("Check worker running for {} on {}".format(self.check_class.__name__, self.ip_addr))
        self.kwargs['ip_addr'] = self.ip_addr
        self.kwargs['points'] = self.points
        check = self.check_class(self.kwargs)
        #if self.kwargs is not None and self.kwargs != {}:
        #    print(self.kwargs)
        #    check = self.check_class(self.ip_addr, self.points, self.kwargs)
        #else:
        #    check = self.check_class(self.ip_addr, self.points)
            
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
            httpCheck = Worker(HTTPCheck, HTTP_SERVER, HTTP_POINTS, uri=HTTP_URI)
            httpCheck.start()
            threads.append(httpCheck)

            # DNS Check Thread
            info("Spawning DNS check worker", "engine")
            dnsCheck = Worker(DNSCheck, DNS_SERVER, DNS_POINTS)
            dnsCheck.start()
            threads.append(dnsCheck)

            # SSH Check Thread
            info("Spawning SSH check worker", "engine")
            sshCheck = Worker(SSHCheck, SSH_SERVERS, SSH_POINTS, user=SSH_USER, password=SSH_PASSWORD)
            sshCheck.start()
            threads.append(sshCheck)

            # FTP Check Thread
            info("Spawning FTP check worker", "engine")
            ftpCheck = Worker(FTPCheck, FTP_SERVER, FTP_POINTS, user=FTP_USER, password=FTP_PASSWORD)
            ftpCheck.start()
            threads.append(ftpCheck)

            # ICMP Check Thread
            info("Spawning ICMP check worker", "engine")
            icmpCheck = Worker(ICMPCheck, ICMP_SERVERS, ICMP_POINTS)
            icmpCheck.start()
            threads.append(icmpCheck)

            # Wait for checks to complete
            for t in threads:
                t.join()

            info("All checks completed", "engine")

            delta = random.randrange(-CHECK_DELTA, CHECK_DELTA)
            time.sleep(CHECK_DELAY + delta)
