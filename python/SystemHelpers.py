import logging

LOG_FILE_DEBUG ='log_debug.txt'
LOG_FILE_INFO ='log_info.txt'
LOG_FILE_WARNING ='log_warning.txt'
FORMAT_LOG = '%(asctime)s - %(message)s'

try:
    logging.basicConfig(format=FORMAT_LOG,filename=LOG_FILE_DEBUG, level=logging.DEBUG)
    logging.basicConfig(format=FORMAT_LOG, filename=LOG_FILE_INFO, level=logging.INFO)
    logging.basicConfig(format=FORMAT_LOG, filename=LOG_FILE_WARNING, level=logging.WARNING)
except:
    pass

def log_debug(message):
    try:
        logging.debug(message)
    except:
        pass
def log_generic_exception_debug(e):
    try:
        logging.debug(str(e))
    except:
        pass

def log_info(message):
    try:
        logging.info(message)
    except:
        pass
def log_generic_exception_info(e):
    try:
        logging.info(str(e))
    except:
        pass

def log_warning(message):
    try:
        logging.warning(message)
    except:
        pass
def log_generic_exception_warning(e):
    try:
        logging.warning(str(e))
    except:
        pass