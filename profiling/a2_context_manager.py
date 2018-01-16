"""
Of course, you can get even more clever with by doing something with a context manager, giving you checkpoints and other good bits to work with:
"""

import time


class timewith():
    def __init__(self, name=''):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name=''):
        print('{timer} {checkpoint} took {elapsed} seconds'.format(
            timer=self.name,
            checkpoint=name,
            elapsed=self.elapsed,
        ).strip())

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('finished')
        pass


def get_number():
    for x in range(5000000):
        yield x


def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result!'

with timewith('fancy thing') as timer:
    expensive_function()
    timer.checkpoint('done with something')
    expensive_function()
    expensive_function()
    timer.checkpoint('done with something else')

# outputs:
# fancy thing done with something took 0.8504540920257568 seconds
# fancy thing done with something else took 2.5682098865509033 seconds
# fancy thing finished took 2.56825590133667 seconds


timer = timewith('fancy thing')
expensive_function()
timer.checkpoint('done with something')

# outputs:
# fancy thing done with something took 0.8459329605102539 seconds
