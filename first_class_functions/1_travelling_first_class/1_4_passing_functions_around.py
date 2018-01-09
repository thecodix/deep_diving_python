"""
Because functions are objects you can pass them as arguments to other functions.

Here’s a greet function that formats a greeting string using the function object
 passed to it and then prints it
"""


def yell(text):
    return text.upper() + '!'


def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

# You can influence the resulting greeting by passing in different functions.
# Here’s what happens if you pass the yell function to greet

greet(yell)
# outputs
# HI, I AM A PYTHON PROGRAM!


# Of course you could also define a new function to generate a different
# flavor of greeting

def whisper(text):
    return text.lower() + '...'

greet(whisper)
# outputs
# hi, i am a python program...


# Here’s how you might format a sequence of greetings all at once
# by mapping the yell function to them

print(list(map(yell, ['hello', 'hey', 'hi'])))
# outputs
# ['HELLO!', 'HEY!', 'HI!']
