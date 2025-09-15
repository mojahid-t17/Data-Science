import logging

logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s- %(name)s- %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.FileHandler('app1.log'),
                logging.StreamHandler()
            ]
            
            )
logger=logging.getLogger("ArithematicApp")

def add(a,b):
    result=a+b
    logging.debug(f"adding {a}+{b}={result}")
    return result

def divide(a,b):
    result=a-b
    logging.debug(f"subtructing {a}-{b}={result}")
    return result
def division(a,b):
    try:
      result=a/b
      logging.debug(f"dividing {a}/{b}={result}")
    except ZeroDivisionError:
        logging.error("division by zero error")
        return None
add(10,22)
divide(12,4)
division(30,0)

    

