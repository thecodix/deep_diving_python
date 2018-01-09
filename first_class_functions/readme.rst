Functions are first class objects
=================================

A first class object is an entity that can be dynamically created,
 destroyed, passed to a function, returned as a value, and have all the
  rights as other variables in the programming language have.

Python’s functions are first-class objects.

Grokking these concepts intuitively will make understanding advanced
 features in Python like lambdas and decorators much easier.
 It also puts you on a path towards functional programming techniques.


Key Takeaways
-------------

Everything in Python is an object, including functions.
You can assign them to variables, store them in data structures,
 and pass or return them to and from other functions (first-class functions.)

First-class functions allow you to abstract away and pass around behavior
 in your programs.

Functions can be nested and they can capture and carry some of the parent
 function’s state with them. Functions that do this are called closures.

Objects can be made callable which allows you to treat them like functions
 in many cases.