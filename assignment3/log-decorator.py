
# #Task1 Declare a decorator called logger_decorator.  

import logging

def logger_decorator(func):
    logger = logging.getLogger(__name__ + "_parameter_log")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(logging.FileHandler("./decorator.log","a"))
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        
    
        # To write a log record:
        logger.log(logging.INFO, f"function: {func.__name__}")

        if (args):
            logger.log(logging.INFO, f"positional parameters: {list(args)}")
        else:
            logger.log(logging.INFO, f"positional parameters: none")

        if(kwargs):
            logger.log(logging.INFO, f"keyword parameters: {dict(kwargs)}")
        else:
            logger.log(logging.INFO, f"keyword parameters: none")

        logger.log(logging.INFO, f"return: {result}")

        return result

    return wrapper

@logger_decorator
def print_only():
    print("I return nothing")

print_only()

@logger_decorator
def positional_args(*args):
    return True

positional_args(12, 3, 778, 99) 

@logger_decorator
def keyw_args(**kwargs):
    return logger_decorator

keyw_args(key1= 122, key2=3444, key3 = 555)
