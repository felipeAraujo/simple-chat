import logging

LOG_FILE_DEBUG ='log_debug.txt'
LOG_FILE_INFO ='log_info.txt'
LOG_FILE_WARNING ='log_warning.txt'
FORMAT_LOG = '%(asctime)s - %(message)s'

logging.basicConfig(format=FORMAT_LOG,filename=LOG_FILE_DEBUG, level=logging.DEBUG)
logging.basicConfig(format=FORMAT_LOG, filename=LOG_FILE_INFO, level=logging.INFO)
logging.basicConfig(format=FORMAT_LOG, filename=LOG_FILE_WARNING, level=logging.WARNING)

def log_debug(message):
    logging.debug(message)

def log_info(message):
    logging.info(message)