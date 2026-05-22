from time import time
from functools import wraps


def with_debug(func):
    debug_arg_name = 'DEBUG'
    @wraps(func)
    def debug_info(*args, **kwargs):
        kwargs_copy = kwargs.copy()
        kwargs_copy.pop(debug_arg_name, None)
        res = func(*args, **kwargs_copy)
        if debug_arg_name in kwargs:
            del kwargs[debug_arg_name]
            print(f"***\t{time()}: calling {func.__name__}")
            print(f"\targs={args} kwargs={kwargs}")
            print(f"\tResult returned: {res}")
        return res
    return debug_info

@with_debug
def adder(a, b):
    return a + b

print('with debug:', adder(1, 2, DEBUG='Yes'))
print('no debug:', adder(3, 4))
print('with debug:', adder(5, 6, DEBUG=None))
