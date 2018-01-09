"""
Objects arn’t functions in Python.

But they can be made callable, which allows you to treat them like functions
 in many cases.

If an object is callable it means you can use round parentheses () on it
 and pass function call arguments to it.

Here’s an example of a callable object
"""


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)

print(plus_3(4))
# outputs: 7


# Behind the scenes, “calling” an object instance as a function attempts
#  to execute the object’s __call__ method.

# Of course not all objects will be callable.
# That’s why there’s a built-in callable function to check whether an object
#  appears callable or not:

print(callable(plus_3))
# True

print(callable(False))
# False
