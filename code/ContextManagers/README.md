## 3 Ways to create Context Managers in Python

### Some Basic Points About Context Managers
* Usually, a Context Manager consists of two magic methods: `__enter__` and `__exit__`.
* The `with` statement calls the Context Manager.
* The `with` statement calls the `__enter__` method and the value returned will be assigned to the variable labeled after the `as` keyword.
* The `__enter__` method doesn’t have to return a value.
* After the `__enter__` method was called, whatever it is inside the with block will be executed then python will call the `__exit__` method


### When to use a Context Manager?
Let say for example you have certain functionality that has preconditions
and post-conditions that need to be met when you execute this functionality. 
That is when a Context Manager appears in the scene.

On a lot of programming books where is shown how to work with files, at 
least it is always mentioned that once you have finished working with a file, 
or any kind of network connection, including connection to databases, 
you have to close it in order to avoid resource leaks.