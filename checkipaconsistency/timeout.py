#  -*- coding: utf-8 -*-
"""
Timeout module

It is used for limiting function execution time.
"""

import signal

class FuncTimeoutException(Exception):
    pass

def handler(signum, _):
    raise FuncTimeoutException('Function Timeout')

def func_timeout(times=0):
    def decorator(func):
        if not times:
            return func
        def wraps(*args, **kwargs):
            signal.alarm(times)
            result = func(*args, **kwargs)
            signal.alarm(0)
            return result
        return wraps
    return decorator

signal.signal(signal.SIGALRM, handler)
