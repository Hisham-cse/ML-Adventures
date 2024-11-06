from logger import logging

def add(a,b):
    logging.debug("The addition is taking place")
    return a+b

logging.debug("The Addition operation is Called")
add(10,15)