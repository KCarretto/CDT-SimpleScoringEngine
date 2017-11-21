"""
A module for checking Mail uptime.
"""
from smtplib import SMTP
from email.mime.text import MIMEText
from enginecheck import EngineCheck

class SMTPCheck(EngineCheck):
    def __init__(self, ip_addr, points, user, password):
        self.user = user
        self.password = password
        self.ip_addr = ip_addr
        EngineCheck.__init__('SMTP', self.ip_addr, points)
    
    def run_check(self):
        sender_address = "{}@chucke.cheese".format(self.user)
        recipient_address = "daryl@chucke.cheese"
        message = MIMEText("Another day another dollar")
        message['Subject'] = "Hey there neighbor"
        message['From'] = sender_address
        message['To'] = recipient_address
        try:
            smtp = SMTP(self.ip_addr)
            smtp.login(self.user, self.password)
            smtp.sendmail(sender_address, recipient_address, message.as_string())
            smtp.quit()
            return True     
   
        except Exception as e:
            return str(e)
