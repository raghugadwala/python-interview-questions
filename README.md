# Python Interview Questions

<details>
<summary>What is the difference between list and tuples in Python?</summary><br><b>
  
* Lists
  * Lists are mutable i.e they can be edited.	
  * Lists are slower than tuples.	
  * List Syntax: list_1 = [10, ‘Chelsea’, 20]
* Tuple
  * Tuples are immutable (tuples are lists which can’t be edited).
  * Tuples are faster than list.
  * Tuple Syntax: tup_1 = (10, ‘Chelsea’ , 20)
</b></details>

<details>
<summary>Python datatypes</summary><br><b>
  
  * inters
  * float
 </b></details>
 <details>
<summary>What type of language is python? Programming or scripting?</summary><br><b>
 Python is capable of scripting, but in general sense, it is considered as a general-purpose programming language.
 </b></details>

<details>
<summary>Python an interpreted language. Explain</summary><br><b>
An interpreted language is any programming language which is not in machine-level code before runtime. Therefore, Python is an interpreted language.
An Interpreted language executes its statements line by line
 </b></details>

<details>
<summary> What is pep 8? PyPI ? PIP </summary><br><b>
PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.
PIP - package installer for python
PyPI - python package idex

</b></details>

<details>
<summary>How is memory managed in Python?</summary><br><b>
  
  Memory is managed in Python in the following ways:  
  
    * Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead
    *  The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code
    *  Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.

</b></details>

<details>
<summary>What is namespace in Python?</summary><br><b>
A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.
</b></details>

<details>
<summary>What are local variables and global variables in Python?</summary><br><b>
  
* Global Variables:
  * Variables declared outside a function or in global space are called global variables. These variables can be accessed by any function in the program.
* Local Variables:
  * Any variable declared inside a function is known as a local variable. This variable is present in the local space and not in the global space.
</b></details>

<details>
<summary>Is indentation required in python?</summary><br><b>
Indentation is necessary for Python. It specifies a block of code. All code within loops, classes, functions, etc is specified within an indented block. 

</b></details>

<details>
<summary>What are functions in Python?</summary><br><b>
A function is a block of code which is executed only when it is called. To define a Python function, the def keyword is used.
</b></details>

<details>
<summary>What is __init__?</summary><br><b>
  __init__ is a method or constructor in Python. This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method.

</b></details>

<details>
<summary>What is a lambda function?</summary><br><b>
An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement.
  Example:
  
  	a = lambda x,y : x+y
    print(a(5, 6))
 
 </b></details>
 
<details>
<summary>What is GIL?</summary><br><b>
   GIL or the Global Interpreter Lock is a mutex, used to limit access to Python objects. It synchronizes threads and prevents them from running at the same time.
</b></details>

<details>
<summary>What is the use of %s?</summary><br><b>
   %s is a format specifier which transmutes any value into a string.
	 
	 str="raghu"
         print('hello %s' % str )   # hello raghu
</b></details>

<details>
<summary>Explain how the python GC (Gargabe collection) works?</summary><br><b>
  GC will do the Refcounting, GC keeps track of how many variables are referencing a memory location.
  If drop to 0, It keeps of that memory location.
	
	Viewing reference counts in Python:
	
	>>> import sys
	>>> a = 'my-string'
	>>> sys.getrefcount(a)
	2
	
	Notice that there are two references to our variable a. One is from creating the variable. The second is when we pass the variable a to the sys.getrefcount() function.
</b></details>
