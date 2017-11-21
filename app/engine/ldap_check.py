"""
A module for checking HTTP uptime.
"""
import ldap

from enginecheck import EngineCheck

class LDAPCheck(EngineCheck):
    def __init__(self, params):
        self.user = params['user']
        self.password = params['password']
        self.user_dn = params['user_dn']
        self.base_dn = params['base_dn']
        EngineCheck.__init__(self, 'LDAP', params['ip_addr'], params['points'])
    
    def run_check(self):
        try:
            l = ldap.initialize('ldap://{}:389'.format(self.ip_addr))
            l.set_option(ldap.OPT_NETWORK_TIMEOUT, self.timeout)
            l.simple_bind_s(self.user, self.password)
            return True

        except Exception as e:
            return str(e)
