Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #swapping of 2 varibles
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print(a,b)
20 10
>>> a=10
>>> b=20
>>> c=a
>>> a=b
>>> b=c
>>> print(a,b)
20 10
>>> a=10
>>> b=20
>>> print(b,a)
20 10
>>> a=10
>>> b=20
>>> a.copy(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.copy(b)
AttributeError: 'int' object has no attribute 'copy'
