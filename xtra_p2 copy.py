import doctest
import logging

# Setup logger
def setup_logger(filename):
    logger = logging.getLogger(filename)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger, filename

logger, logname = setup_logger(__file__)

# Decorator to log function calls and results
def log_function(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

# TODO: Implement the function as described
@log_function
def transform_using_keyword_args_with_default_values(input="bearcat", reverse=False):
    '''Return a string with just the first 3 letters of input string. 
    If reverse is True, reverse the first 3 letters. 
    If reverse is omitted or False, return the first 3 letters reversed. 
    @kwargs:
        input: a string, default "bearcat"
        reverse: a boolean, default False'''
    
    result = input[:3]
    
    if reverse:
        result = result[::-1]

    return result

if __name__ == "__main__":
    transform_using_keyword_args_with_default_values()
    transform_using_keyword_args_with_default_values(reverse=True)
    transform_using_keyword_args_with_default_values(input="hello", reverse=True)

    logger.info("===========================================================")
    logger.info("Running doctest.testmod() function to unit test our code")
    logger.info("===========================================================")

    doctest_result = doctest.testmod()
    if doctest_result.failed == 0:
        logger.info("All tests passed!")
    else:
        logger.error(f"{doctest_result.failed} tests failed!")

    logger.info("Script complete. More info in the log file.")
