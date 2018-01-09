"""
As functions are first-class citizens you can store them in data structures,
 just like you can with other objects.
"""


def yell(text):
    return text.upper() + '!'

bark = yell

# For example, you can add functions to a list

funcs = [bark, str.lower, str.capitalize]
print(funcs)
# outputs
# [<function yell at 0x100762e18>, <method 'lower' of 'str' objects>, <method 'capitalize' of 'str' objects>]


# Accessing the function objects stored inside the list works like it would
# with any other type of object:

for f in funcs:
    print(f('hey there'))
# outputs
# <function yell at 0x10ff96510> 'HEY THERE!'
# <method 'lower' of 'str' objects> 'hey there'
# <method 'capitalize' of 'str' objects> 'Hey there'

# You can even call a function object stored in the list without assigning
# it to a variable first.
# You can do the lookup and then immediately call the resulting
#  “disembodied” function object within a single expression:

print(funcs[0]('heyho'))
# outputs
# HEYHO!
