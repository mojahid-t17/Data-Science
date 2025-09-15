from logger import logging

def add(a,b):
    logging.debug('addition operation is taking place')
    return a+b

add(20,30)
logging.debug('addition function is called ')