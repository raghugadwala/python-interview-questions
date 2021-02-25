## 3 Ways to create Context Managers in Python

### Some Basic Points About Context Managers
* Usually, a Context Manager consists of two magic methods: `__enter__` and `__exit__`.
* The `with` statement calls the Context Manager.
* The `with` statement calls the `__enter__` method and the value returned will be assigned to the variable labeled after the `as` keyword.
* The `__enter__` method doesn’t have to return a value.
* After the `__enter__` method was called, whatever it is inside the with block will be executed then python will call the `__exit__` method