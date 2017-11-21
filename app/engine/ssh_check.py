"""
A module for checking SSH connection and run a command
"""
import paramiko

from enginecheck import EngineCheck

class SSHCheck(EngineCheck):
    def __init__(self, ip_addr, points, user, password):
        self.user = user
        self.password = password
        EngineCheck.__init__('SSH', ip_addr, points)
    
    def run_check(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        command = 'ls -l'
        try:
            ssh.connect(self.ip_addr, username=self.user, password=self.password, timeout=5)
            stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
            ssh.close()
            return True        
        except Exception as e:
            return str(e)
