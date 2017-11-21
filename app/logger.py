from .config import LOG_LEVEL

def debug(msg, application=None):
    if LOG_LEVEL.lower() == 'debug':
        _log("DEBUG", msg, application)

def info(msg, application=None):
    if LOG_LEVEL.lower() in ['debug', 'info']:
        _log("INFO", msg, application)

def warn(msg, application=None):
    if LOG_LEVEL.lower() in ['debug', 'info', 'warn']:
        _log("WARN", msg, application)

def error(msg, application=None):
    if LOG_LEVEL.lower() in ['debug', 'info', 'warn', 'error']:
        _log("ERROR", msg, application)

def crit(msg, application=None):
    if LOG_LEVEL.lower() != 'none':
        _log("CRITICAL", msg, application)

def _log(level, msg, application=None):
    print("{}:{}:\t{}".format(level, application, msg))
