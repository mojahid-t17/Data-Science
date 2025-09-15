import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='test.log',filemode='w',format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
# logging message with different levels
logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is a error message')