
# #Task1 Declare a decorator called logger_decorator.  
# This should log the name of the called function (func.__name__), 
# the input parameters of that were passed, and the value the function returns,
#  to a file ./decorator.log. 
#  (Logging was described in lesson 1, so review this if you need to do so.)  
# Functions may have positional arguments, keyword arguments, both, or neither. 
#  So for each invocation of a decorated function, the log would have:
# function: <the function name>
# positional parameters: <a list of the positional parameters,
#  or "none" if none are passed>
# keyword parameters: <a dict of the keyword parameters, 
# or "none" if none are passed>
# return: <the return value>
import logging

def logger_decorator(func):
    logger = logging.getLogger(__name__ + "_parameter_log")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(logging.FileHandler("./decorator.log","a"))
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        
    
        # To write a log record:
        logger.log(logging.INFO, f"function:{func.__name__}")

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
def positional_args(var1, var2, var3, var4):
    return True

positional_args(12, 3, 778, 99) 

@logger_decorator
def keyw_args(key1=0, key2=0, key3=3):
    return logger_decorator

keyw_args(key1= 122, key2=3444, key3 = 555)
