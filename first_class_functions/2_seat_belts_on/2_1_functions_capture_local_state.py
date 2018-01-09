"""
Not only can functions return other functions, these inner functions can also
 capture and carry some of the parent function’s state with them.

We will slightly rewrite the previous get_speak_func example to illustrate this.
The new version takes a “volume” and a “text” argument right away to make
the returned function immediately callable
"""


def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func('Hello, World', 0.7)())
# outputs
# HELLO, WORLD!

# Take a good look at the inner functions whisper and yell now.
# Notice how they no longer have a text parameter?
# But somehow they can still access the text parameter defined in the parent function.
# In fact, they seem to capture and “remember” the value of that argument.

# Functions that do this are called lexical closures (or just closures, for short).
# A closure remembers the values from its enclosing lexical scope even
# when the program flow is no longer in that scope


# In practical terms this means not only can functions return behaviors
# but they can also pre-configure those behaviors.

# Here’s another bare-bones example to illustrate this idea:

def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
# output: 7

print(plus_5(4))
# output: 9

# Notice how the “adder” functions can still access the n argument
#  of the make_adder function (the enclosing scope)
