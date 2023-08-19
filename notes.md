# Python Notes

## Variables

Python variables can't start with a number.

Variables can't start with a number, but can contain numbers.

Variables can't contain spaces, but can contain underscores.

Variables can't contain special characters, but can contain underscores.

They can't be Python keywords. Like 'list' or 'str' or 'for'.

Variables are case sensitive. 'a' is different from 'A'.
It's is dynamically typed. You don't need to specify the type of the variable.

Whole words should be separated by an underscore. Be verbose with your variable names.

`type()` is a function that returns the type of the variable.

`none` is a special type in Python. It's used to represent the absence of a value. It is the same as `null` in other languages.

```python
>>> x = None
>>> type(x)
>>> <class 'NoneType'>
```

The above is a snippet from the Python interpreter. The `>>>` is the prompt. The `x = None` is the command. The `type(x)` is the output. The `<class 'NoneType'>` is the type of the variable.

## Numbers

There are three types of numbers in Python. Integers, floating point numbers and complex numbers.

Integers are whole numbers. Floating point numbers are numbers with decimal points. Complex numbers are numbers with imaginary parts.

```python
>>> # Integers
>>> x = 4
>>> y = -3938
>>> z = 0
```

Just add a decimal point to make it a floating point number.

```python
>>> x = 5.0
>>> y = -3484.5
>>> z = 0.0
>>> z
0.0
>>>type(z)
<class 'float'>
```

Python also has complex numbers. Complex numbers are numbers with imaginary parts. The imaginary part is denoted by `j`.

```python
>>> x = 42j
>>> x
42j
>>> type(x)
<class 'complex'>
```

Here's a another check for the type of the variable.

```python
>>> type(y)
<class 'float'>
>>> type(1)
<class 'int'>
```

```python
>>> x = 5
>>> y = 3.0
>>> x + y
8.0
```

In this example, an integer and a floating point number are added. The result is a floating point number.

```python
>>> 6 / 2
3.0
>>>
```

Note that dividing by an integer returns a floating point number.

## Strings

Strings are sequences of characters. They are enclosed in single quotes or double quotes.

```python
>>> 'Hello'
'Hello'
>>> "Hello"
'Hello'
>>>
```

It's generally best practice to use double quotes. That way you can avoid escaping single quotes.

You can define a string with triple quotes. This is useful for multi-line strings.

```python
>>> long_string = """
... 12345
... abc
... """
>>> long_string
'\n12345\nabc\n'
```

There are several types of string formatting. The most common is the `format()` method.

Here is an example of an 'f-string'. It's a new way of formatting strings in Python 3.6.

```python
>>> name = "Nina"
>>> f"Hello, {name}"
'Hello, Nina'
```

```python
salutation = "Hello "
name = "Nina"
greeting = salutation + name
# The value of greeting will be "Hello Nina"
```

### Common mistakes

Not closing the quotes properly.

```python
>>> name = 'Nina"
  File "<stdin>", line 1
    name = 'Nina"
                 ^
SyntaxError: EOL while scanning string literal
```

If you try to concatenate a string and a number, you'll get an error.

```python
>>> "Hello, " + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

### Practice

Use the `type()` function to check the type of the following variables.

```python
>>> x = 42
>>> y = 3 / 4
>>> z = int('7')
>>> a = float(5)
>>> name = "Nina"
```

Output:

```python
>>> type(x)
>>> <class 'int'>
>>> type(y)
>>> <class 'float'>
>>> type(a)
>>> <class 'float'>
>>> type(name)
>>> <class 'str'>
```

f-strings are the new way of formatting strings in Python and are recommended over the older methods.

```python
>>> name = 'Wanda'
>>> print(f"My name is {name} and I am a dog")
My name is Wanda and I am a dog
```

Here's a way to calculate the rent per day from the monthly rent.

```python
My name is Wanda and I am a dog
>>> rent = 5000
>>> per_day = rent / 30
>>> per_day
166.66666666666666
>>> print(per_day)
166.66666666666666
>>>
```

Here is the old way of formatting strings. It's not recommended.

```python
>>> name = 'Wanda'
>>> print("My name is %s and I am a dog" % name)
My name is Wanda and I am a dog
```

Two different ways to use print to print a string.

```python
# using a comma
>>> print("My name is", name)
My name is Wanda
# using an f-string
>>> print(f"My name is {name}.")
My name is Wanda.

```

```python
>>> print (f"My name is {name} and I pay ${ rent / 30} / day in rent")
My name is Bill the Programmer and I pay $166.66666666666666 / day in rent
```

Python has a few built-in functions to help you if you get stuck. `type()` tells you what an object’s type is, for example a string `(str)` or integer `(int)`. `dir()` returns a list of valid attributes for an object, so you can quickly see what variables an object has or what functions you can call on it. `help()` brings up helpful documentation on any object. You can also type `help()` on its own to bring an interactive help console.

Here's an example of using `dir()`.

```python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

It shows all the available methods for the string class.

Here's an example of using `dir()` on an integer.

```python
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

Here's an example of using `help()`.

```python
>>> help(str)
Help on class str in module builtins:
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
```

And so on.

Using help on a specific method.

```python
>>> help(int.real)
Help on getset descriptor builtins.int.real:

real
    the real part of a complex number
(END)
```
