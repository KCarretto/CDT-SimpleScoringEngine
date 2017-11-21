"""
A module for checking SMTP uptime.
"""
from smtplib import SMTP
from email.mime.text import MIMEText
from enginecheck import EngineCheck

class SMTPCheck(EngineCheck):
    def __init__(self, params):
        self.user = params['user']
        self.password = params['password']
        EngineCheck.__init__(self, 'SMTP', params['ip_addr'], params['points'])
    
    def run_check(self):
        sender_address = "{}@chucke.cheese".format(self.user)
        recipient_address = "daryl@chucke.cheese"
        message = MIMEText("Another day another dollar")
        message['Subject'] = "Hey there neighbor"
        message['From'] = sender_address
        message['To'] = recipient_address
        try:
            smtp = SMTP(self.ip_addr, timeout=self.timeout)
            smtp.login(self.user, self.password)
            smtp.sendmail(sender_address, recipient_address, message.as_string())
            smtp.quit()
            return True     
   
        except Exception as e:
            return str(e)
