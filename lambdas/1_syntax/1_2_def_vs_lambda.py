"""
The lambda function is a minimal function that quickly defines a single line,
borrowed from Lisp and can be used wherever a function is needed.

The following example compares the traditional def definition with lambda
"""


def product(x, y):
    return x * y

print(product(2, 3))
# outputs: 6

fancy_lambda = lambda x, y: x * y

print(fancy_lambda(2, 3))
# outputs: 6
