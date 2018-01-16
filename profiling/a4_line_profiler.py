"""
If the built-in profile was a big gun, consider the line profiler an Ion cannon.
 It is quite heavy and powerful (and a lot of fun to use!).

For this example, we'll use the great kernprof line-profiler available as a handy
 line_profiler PyPi package.

For ease of use, we'll wrap it once again in a decorator that simplifies usage
as well as provides a way to protect us from leaving it in production
 (because it is dog slow!).
"""

try:
    from line_profiler import LineProfiler

    def do_profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner

except ImportError:
    def do_profile(follow=[]):
        "Helpful if you accidentally leave in production!"
        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return inner


def get_number():
    for x in range(5000000):
        yield x


@do_profile(follow=[get_number])
def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result!'

result = expensive_function()

# The output will be something like this

"""
Timer unit: 1e-06 s

Total time: 3.89542 s
File: profiling/a4_line_profiler.py
Function: get_number at line 41

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    41                                           def get_number():
    42   5000001    2040744.0      0.4     52.4      for x in range(5000000):
    43   5000000    1854675.0      0.4     47.6          yield x

Total time: 14.1145 s
File: profiling/a4_line_profiler.py
Function: expensive_function at line 46

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    46                                           @do_profile(follow=[get_number])
    47                                           def expensive_function():
    48   5000001   11511196.0      2.3     81.6      for x in get_number():
    49   5000000    2603306.0      0.5     18.4          i = x ^ x ^ x
    50         1          2.0      2.0      0.0      return 'some result!'
"""
