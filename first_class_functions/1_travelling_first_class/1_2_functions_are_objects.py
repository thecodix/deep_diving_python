"""
All data in a Python program is represented by objects or relations
 between objects. Things like strings, lists, modules, and functions
  are all objects.
  There’s nothing particularly special about functions in Python.

Because the yell function is an object in Python you can assign it
 to another variable, just like any other object
"""


def yell(text):
    return text.upper() + '!'

# This line doesn’t call the function.
# It takes the function object referenced by yell and creates
#  a second name pointing to it, bark

bark = yell

print(bark('woof'))
# outputs
# WOOF!


# Function objects and their names are two separate concerns.
#
# Here’s more proof: You can delete the function’s original name (yell).
#   Because another name (bark) still points to the underlying function
#    you can still call the function through it

del yell

try:
    print(yell('hello?'))
except NameError as error:
    print(error)
# outputs
# name 'yell' is not defined

print(bark('hey'))
# outputs
# 'HEY!'


# By the way, Python attaches a string identifier to every function
#  at creation time for debugging purposes. You can access this internal
#   identifier with the __name__ attribute:

print(bark.__name__)
# outputs
# 'yell'

# While the function’s __name__ is still “yell” that won’t affect how you
#  can access it from your code.
# This identifier is merely a debugging aid
