"""
Both the function and the caller refer to the same object in memory,
so when the append function adds an extra item to the list, we see this
 in the caller too!

 They’re different names for the same thing; different boxes containing the same
  object. This is what is meant by passing the object references by value -
  the function and caller use the same object in memory, but accessed through
  different variables.

This means that the same object is being stored in multiple different boxes,
 and the metaphor kind of breaks down.

 Pretend it’s quantum or something
"""


def appending(my_list):
    print("list before", my_list)
    my_list.append(1)
    print("list after", my_list)

my_list = [0]
appending(my_list)
print("end of function call", my_list)
# outputs
# list before [0]
# list after [0, 1]
# end of function call [0, 1]
