from functools import wraps


def deprecated(use_instead_func):
    def deco(func):
        @wraps(func)
        def print_deprecated_info(*args, **kwargs):
            print(f"!!! {func.__name__} is bad use {use_instead_func} instead !!!")
            return func(*args, **kwargs)
        return print_deprecated_info
    return deco


@deprecated('good_add')
def bad_add(a, b):
    return a + b

@deprecated('awesome_fun')
def pathetic_fun(*, a, b):
    return a * b

c = bad_add(1, 7)
print(f'{c=}')
d = pathetic_fun(a=3, b=7)
print(f'{d=}')