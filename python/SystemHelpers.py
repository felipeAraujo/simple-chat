import logging

LOG_FILE_DEBUG ='log_debug.txt'
LOG_FILE_INFO ='log_info.txt'
LOG_FILE_WARNING ='log_warning.txt'
FORMAT_LOG = '%(asctime)s - %(message)s'

def log_debug(message):
    try:
        logging.basicConfig(format=FORMAT_LOG,filename=LOG_FILE_DEBUG, level=logging.DEBUG)
        logging.debug(message)
    except:
        pass
def log_warning(e):
    try:
        logging.basicConfig(format=FORMAT_LOG, filename=LOG_FILE_WARNING, level=logging.WARNING)
        logging.waning(str(e))
    except:
        pass

def log_info(message):
    try:
        logging.basicConfig(format=FORMAT_LOG, filename=LOG_FILE_INFO, level=logging.INFO)
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