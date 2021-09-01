# Create a decorator that makes sure that all function arguments where it's applied
# will match the regex on the regex exercise above
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__} ({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value}")
        return value
    return wrapper_decorator


import re

@decorator
def match_pattern(pattern, str):
    return re.findall(pattern, str, flags=0)



pattern = "[a-z]+_[a-z]+"
str = 'a-b-c123456789a-b-c1236123465aad_eeee1232134565aaa_bbfff125444i_iii123456'

print("result: ", match_pattern(pattern,str))

