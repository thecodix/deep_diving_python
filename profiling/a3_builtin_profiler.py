"""
Breaking out the built-in profiler is akin to breaking out the big guns.
It is extremely powerful, but a little unwieldy and sometimes a bit difficult
 to interpret and act on.

You can read a bit more about the built-in profile module but the basics are
 quite simple: you enable and disable the profiler and it logs all function calls
  and execution times. It can then compile and print the output for you.

A quick decorator simplifies this

Built-in Pros: No external dependencies and quite fast.
Useful for quick high-level checks.

Built-in Cons: Rather limited information that usually requires deeper debugging;
 reports are a bit unintuitive, especially for complex codebases.
"""

import cProfile


def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func


def get_number():
    for x in range(5000000):
        yield x


@do_cprofile
def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result!'

# perform profiling
result = expensive_function()

# output will be something like this

"""
        5000003 function calls in 1.545 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  5000001    0.529    0.000    0.529    0.000 a3_builtin_profiler.py:29(get_number)
        1    1.016    1.016    1.545    1.545 a3_builtin_profiler.py:34(expensive_function)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
