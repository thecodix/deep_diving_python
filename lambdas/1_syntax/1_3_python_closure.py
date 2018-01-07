"""
Let’s take v1 as an example to illustrate the closure:

1) The function start_at_v1 takes 1 argument and returns 1 function object.
  The behavior of this function object is implemented by nested function increment_by.

2) For the function increment_by, the variable x is the so-called
  non-local variable (since x is neither a local variable nor a generic variable),
  increment_by implements the function’s behavior and returns.

3) Main entrance c1 received the return value as a function object,
  from the id (increment_by) == id (c1) can be concluded

4) Benefit from Python’s support for closures, where objects pointed
  to by c1 can access non-local variables that are not within the scope
  of their function, as opposed to ordinary function objects. This variable
  is incremented by the outer wrapper function start_at_v1 of increment_by.

  Which is equivalent to c1 point to the function of the object function
  of its outer wrapping function into the Senate has a “memory” function,
  by calling the outer wrapper function to create closures, different parameters
  into the reference function is the inner environment Maintenance up.

5) When c1 (3) is called, the passed parameters are evaluated together
  with the parameters of the outer wrapper function maintained by the
  reference environment to obtain the final result.
"""


def start_at_v1(x):
    def increment_by(y):
        return x + y

    print('id(increment_by)=%s' % (id(increment_by)))
    return increment_by


def start_at_v2(x):
    return lambda y: x + y


if '__main__' == __name__:
    c1 = start_at_v1(2)
    print('type(c1)=%s, c1(3)=%s' % (type(c1), c1(3)))
    print('id(c1)=%s' % (id(c1)))

    c2 = start_at_v2(2)
    print('type(c2)=%s, c2(3)=%s' % (type(c2), c2(3)))

# Outputs:
# id(increment_by)=139730510519782
# type(c1)=<type 'function'>, c1(3)=5
# id(c1)=139730510519782
# type(c2)=<type 'function'>, c2(3)=5
