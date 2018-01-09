"""
Python allows functions to be defined inside other functions.

These are often called nested functions or inner functions
"""


def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

print(speak('Hello, World'))
# outputs
# hello, world...

# Every time you call speak it defines a new inner function whisper and then calls it.

# And here’s the kicker: whisper does not exist outside speak

try:
    print(whisper('Yo'))
except NameError as error:
    print(error)
# outputs
# "name 'whisper' is not defined

try:
    print(speak.whisper)
except AttributeError as error:
    print(error)
# outputs
# 'function' object has no attribute 'whisper'


# But what if you really wanted to access that nested whisper function from
#  outside speak? Well, functions are objects—you can return the inner function
#  to the caller of the parent function.

# For example, here’s a function defining two inner functions.
# Depending on the argument passed to top-level function it selects and returns
#  one of the inner functions to the caller:

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper

# Notice how get_speak_func doesn’t actually call one of its inner functions.
# It simply selects the appropriate function based on the volume argument
# and then returns the function object

print(get_speak_func(0.3))
# <function get_speak_func.<locals>.whisper at 0x10ae18>

print(get_speak_func(0.7))
# <function get_speak_func.<locals>.yell at 0x1008c8>


# Of course you could then go on and call the returned function,
# either directly or by assigning it to a variable name first

speak_func = get_speak_func(0.7)
print(speak_func('Hello'))
# outputs
# 'HELLO!'

# Let that sink in for a second here…
# This means not only can functions accept behaviors through arguments
# but they can also return behaviors.

# How cool is that?
