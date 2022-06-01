# This is a follow along of the YouTube tutorial
# Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
# by Corey Schafer
# https://youtu.be/FsAPt_9Bf3U

# When we use a class as decorator
# We need to pass the original function through the constructor (dunder __init__ method)
# And we need to implement the duncer __call__ method which is essentially going to be decorator function
# __call__ method always needs to pass the args and kwargs to the original function
# and return the execution of the original function
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)

# Simple decorator function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


# wrpas is needed in order to preserve the identity of the original function when returning from the wrapper
from functools import wraps

# Logger decorator that creates a new file for each function that its being called and have been decorated by it
# And logs some info into that file
# then calls the original function
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    # Need to use the wraps() decorator in order to preserve the identity of orig_func
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, *kwargs)

    return wrapper

# Timer decorator that measure the length of the original function call
def my_timer(orig_func):
    import time

    # Need to use the wraps() decorator in order to preserve the identity of orig_func
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper

@decorator_function
def display():
    print('display function ran')

# The above declaration is equivalent to the following:
# decorated_display = decorator_function(display)
# decorated_display()

display()

import time

# because we use the wraps() decorator inside of each of these decorators we can chain them together
# And still have an accurate execution of the display_info function
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran with arguments ({name}, {age})')

print(display_info.__name__)

display_info('Tom', 22)
