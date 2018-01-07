"""
Scoping in Python is lexical.

A closure will always remember the name and scope of the variable,
not the object it's pointing to.

Since all the functions in this example are created in the same scope
and use the same variable name, they always refer to the same variable.
"""

fs = [(lambda n: i + n) for i in range(10)]

print(fs[3](4))

# outputs: 13

# Surprisingly is not 3+4, why?
