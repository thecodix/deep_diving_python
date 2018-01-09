"""
Python is different. As we know, in Python, “Object references are passed by value”.

A function receives a reference to (and will access) the same object in memory as
 used by the caller.

 However, it does not receive the box that the caller is storing this object in;
  as in pass-by-value, the function provides its own box and creates a new variable
   for itself.
"""


def reassign(my_list):
    print("list before", my_list)
    my_list = [0, 1]
    print("list after", my_list)

my_list = [0]
reassign(my_list)
print("end of function call", my_list)
# outputs
# list before [0]
# list after [0, 1]
# end of function call [0]
