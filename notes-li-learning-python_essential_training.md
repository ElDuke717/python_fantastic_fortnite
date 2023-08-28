# Python Essential Training

## Notes for the LinkedIn Learning course

### by Ryan Mitchell

#### Course details

Python is one of the most commonly used dynamic languages for many large organizations, including Google, Yahoo and IBM. Supported on all major operating systems, it comes pre-installed on Macs, as well as most Linux and Unix-based systems. In this course, senior software engineer Ryan Mitchell guides you through all the essentials of learning and using Python. Learn how computers think, as well as how to install Python, pip, and Jupyter Notebook and the basics of writing a program. Explore variables and types, operators, functions, classes, objects, and more. Go over basic data types like ints and floats, Booleans, and strings. Deep dive into basic data structures, control flow, functions, classes, and objects. Find out how to handle errors and exceptions, as well as threads and processes. Plus, discover how to work with different types of files in Python, pass command-line arguments to your Python script, and create modules and packages.

I downloaded the course files from the course repo and add them to this repository.

We set up Jupyter Notebook, which is interesting and new.

## import statement

The import statement is used to import modules into the current namespace. The from form of import can also be used to import specific attributes or functions into the current namespace. For example:

Here's a cool poem we got from the Python interpreter, using the import statement:

```python
(env) nickhuemmer@Nicks-Mac-mini Exercise Files % python
Python 3.9.6 (default, May  7 2023, 23:32:44)
[Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

We wrote a simple program to print "Hello World" to the console.

Jupyter Notebook is a great tool for learning Python. It is a web-based interactive development environment. It is a great tool for learning Python because it allows you to write and run code in the same place.

When you run Jupyter notebook from the command line, what you're really doing is starting a web application on your computer.

They are very popular in the data science community. Since they allow you to make graphs and charts, they are great for data science.

## Jupyter Notebook

Here are some basic commands for Jupyter Notebook:

- run current cell and advance: shift + enter

- run current cell: control + enter

- insert cell above: a

- insert cell below: b

- delete cell: dd

- undo delete cell: z

## Variables and Types

Variables are used to store values. They are like boxes that hold values. You can change the value of a variable at any time.

You can't have a variable with a name like 1x. It has to start with a letter or an underscore.
Variable names start with lowercase letters.

Whole numbers are ints. Numbers with decimals are floats.

Numbers with a j at the end are complex numbers.

Complex numbers are numbers with a real part and an imaginary part.

```
1j * 1j
```

## Data Structures

Data structures are ways of organizing data. They are ways of storing data in a computer.

Sets are unordered collections of unique elements. They are like lists, but they don't have any duplicates. They are unordered, so you can't index them. You can also compare them directly, and if they have the same elements, they are equal, even though they are not in the same order, like lists.

### Lists

just like arrays in other languages, like JavaScript

### Sets

They are groups of unique values. They use curly brackets.

### Tuples

Why do we use them?

- They're memory efficient.
- They're immutable, so they can't be changed.
- Good for storing things that shouldn't be changed.

### Dictionaries

Dictionaries are like objects in JavaScript. They are key-value pairs.

They use curly brackets, like sets.

## Operators

Operators are used to perform operations on variables and values.

Any time you do division, you get a float.

The modulus operator gives you the remainder of a division operation.

Logical operators are used to combine conditional statements. They are and, or, and not. They are represented by the words and, or, and not.

Membership operators are used to test if a sequence is present in an object. They are in and not in.

Identity operators are used to compare the objects, not if they are equal, but if they are the same object, with the same memory location. They are is and is not.

Note that you can multiply a string by a number to repeat it. E.g. 'hello' \* 3 will give you 'hellohellohello'.

## Control Flow

The if statement

```python
a = True
if a:
    print('It is true!')
    print('Also print this')
else:
    print('It is false!')
print('Always print this')

```

It is true!
Also print this
Always print this

### loops

```python
>>> for i in range(10):
...     print(i)
...
0
1
2
3
4
5
6
7
8
9

```

#### while loops

```python
>>> a = 0
>>> while a < 5:
...     print(a)
...     a = a + 1
...
0
1
2
3
4

```

## Classes and Instances

Classes are used to create objects. They are like blueprints for objects.

Objects are instances of classes.

Classes look like functions - but they are not functions and use the class keyword and are uppercase.

Classes are like cookie cutters, and objects are like cookies.

Classes are like factories, and objects are like products.

Classes are like recipes, and objects are like dishes.

Classes are like templates, and objects are like documents.

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')
```

```python
>>> class Dog:
...     def __init__(self, name):
...         self.name = name
...         self.legs = 4
...
...     def speak(self):
...         print(self.name + ' says: Bark!')
>>> my_dog = Dog('Wanda')
>>> my_dog.speak()
Wanda says: Bark!
```

Classes are very similar to how they are in JavaScript. The main difference is that you have to use the self keyword to refer to the object itself (in JavaScript, you use the this keyword).

In Python, **init** is a special method (also called a constructor) that is automatically called when a new instance of a class is created. It's used to initialize the attributes or properties of the object.

`__init__` is the constructor, it is a special method that is automatically called when a new instance of a class is created.

## Ints and Floats

`int()` is a class, not a function.

This is called casting:

```python
# this is called casting, converting one type to another
int(4 ** 4.0)

>>> int(8.9)
8
# When you cast from a float to an int, it truncates the decimal part. It doesn't round it.

# Here you can use the round function to round the output of dividing 14 by 3
>>> round(14/3, 2)
4.67
# Python will only round so far. It won't round to the nearest 100th, for example.  This is called precision and it is a limitation of the float type and has to do with the amount of memory that is allocated to store the number.
>>> 14/3
4.666666666666667
>>>
```

## Other types of numbers - see notebook notes.

## Strings

Note that you can use single or double quotes to create strings.

You can use triple quotes to create multi-line strings.

You can use the backslash to escape characters.

You can use the backslash to escape quotes.

f strings are a way to format strings. They are a way to insert variables into strings.

```python
>>> name = 'Nick'
>>> f'Hello, {name}'
'Hello, Nick'
```

```python
bool(-1) == 1
True
```

In Python, the `bool()` function is used to convert a value to its boolean equivalent. The boolean value `True` is associated with non-zero values, and `False` is associated with zero.

When you pass the integer value `-1` to the `bool()` function, it gets converted to its boolean equivalent. Any non-zero integer is considered `True` in a boolean context.

So, `bool(-1)` evaluates to `True`, and since `True` is represented as `1` in Python, the expression `bool(-1) == 1` is indeed `True`.

## Lists

# Control Flow

## if and else

You can use else, if or elif in place of else if.

```python
def fizzBuzz(num):
    if num % 15 == 0: # you can use 15 rather than checking the modulus against 3 or 5, this is more concise.
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


for num in range(0, 100):
     fizzBuzz(num)
```

Here's a one liner way to check the modulus of three with '
Fizz

```python
for num in range(0, 100):
    print(Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0) or num)
```

## while loops

They can be very dangerous because they can run forever.

```python

wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    print('Still waiting!')

print(f'We are at {wait_until} seconds!')
```

Pass is a way to do nothing. It is used as a placeholder.

```python
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    pass

print(f'We are at {wait_until} seconds!')
```

Break is used to break out of a loop.

```python
wait_until = datetime.now().second + 2

while True:
    if datetime.now().second == wait_until:
        print(f'We are at {wait_until} seconds!')
        break
```

We are at 5 seconds!

Continue is used to skip the rest of the code in a loop and go to the next iteration.

```python
for num in range(0, 100):
    if num % 2 == 0:
        continue
    print(num)
```

## for loops

All statements that can be used for while loops can also be used for for loops.

```python
for num in range(0, 100):
    print(num)
```

## For / Else

```python
for number in range(2, 100):
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f'{number} is prime!')
2 is prime!
3 is prime!
5 is prime!
7 is prime!
11 is prime!
13 is prime!
17 is prime!
19 is prime!
23 is prime!
29 is prime!
31 is prime!
37 is prime!
41 is prime!
43 is prime!
47 is prime!
53 is prime!
59 is prime!
61 is prime!
67 is prime!
71 is prime!
73 is prime!
79 is prime!
83 is prime!
89 is prime!
97 is prime!     
```
