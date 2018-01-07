"""
A way to make this work would be to create a new scope each time you create the lambda

The scope here is created using a new function (a lambda, for brevity),
which binds its argument, and passing the value you want to bind as the argument.

In real code, though, you most likely will have an ordinary function instead
of the lambda to create the new scope
"""

fs = [(lambda n, i=i: i + n) for i in range(10)]

print(fs[3](4))

# outputs: 7

# Profit
