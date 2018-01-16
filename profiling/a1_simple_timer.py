"""
Timers are simple, flexible ways to measure execution time.
You can drop them in just about anywhere and they have very minimal side-effects.

It is quite easy to roll your own timer and even customize it to work exactly how you like.

For example, a simple timing decorator might look like
"""

import time


def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, 'took', end - start, 'time')
        return result
    return f_timer


def get_number():
    for x in range(5000000):
        yield x


@timefunc
def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result!'


result = expensive_function()
# outputs
# "expensive_function took 0.8596758842468262 time"
