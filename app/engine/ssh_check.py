"""
A module for checking SSH connection and run a command
"""
import paramiko

from enginecheck import EngineCheck

class SSHCheck(EngineCheck):
    def __init__(self, params):
        self.user = params['user']
        self.password = params['password']
        ip_addr = ','.join(params['ip_addr'])
        EngineCheck.__init__(self, 'SSH', ip_addr, params['points'])
    
    def run_check(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        command = 'ls -l'
        try:
            for ip in self.ip_addr.split(','):
                ssh.connect(ip, username=self.user, password=self.password, timeout=5)
                stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
                ssh.close()
            return True        
        except Exception as e:
            return str(e)
