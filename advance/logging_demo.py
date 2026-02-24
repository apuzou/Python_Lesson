import logging

fomatter = '%(levelname)s: %(message)s: %(asctime)s'
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=fomatter)

logging.critical('This is a critical message')
logging.error('This is a error message')
logging.warning('This is a warning message')
logging.info('This is a info message')
logging.debug('This is a debug message')
