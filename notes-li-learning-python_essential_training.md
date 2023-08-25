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

