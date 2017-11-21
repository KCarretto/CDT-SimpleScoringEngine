import time

from .config import LOG_LEVEL
from .models.log import Log

def debug(msg, application=None):
    if LOG_LEVEL.lower() == 'debug':
        _log('debug', msg, application)

def info(msg, application=None):
    if LOG_LEVEL.lower() in ['debug', 'info']:
        _log('info', msg, application)

def warn(msg, application=None):
    if LOG_LEVEL.lower() in ['debug', 'info', 'warn']:
        _log('warn', msg, application)

def crit(msg, application=None):
    if LOG_LEVEL.lower() != 'none':
        _log("crit", msg, application)

def _log(level, msg, application=None):
    print("{}:{}:\t{}".format(level, application, msg))
    l = Log(
        timestamp=time.time(),
        application=application,
        level=level,
    )
