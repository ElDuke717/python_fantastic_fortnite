# Python Stuff

## Python Fundamentals

### Python Data Types

There are three data types in Python:

- Numbers
- Strings
- Booleans

This makes it a lot simpler to work with data in Python.

### Variables

Variables are used to store values. A variable is created the moment you first assign a value to it.

#### Naming rules for variables

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number, but numbers can be included in the rest of the name
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot contain spaces
- Variable names should be descriptive (age is better than a)

### Numbers

Python has three numeric types:

- int (signed integers)
- float (floating point real values) (aka decimal numbers), can be positive or negative
- complex (complex numbers)

#### Integers

Integers are whole numbers. They can be positive or negative, but they cannot be decimals.

#### Floats

Floats are real numbers. They can be positive or negative, and they can be decimals.
Floating-point numbers, or floats, refer to positive and negative decimal numbers. Python allows us to create decimals up to a very high decimal place. This ensures accurate computations for precise values.
A float occupies 24 bytes of memory.

#### Complex Numbers

Complex numbers are numbers with a real and imaginary part. The imaginary part is written with a "j"

> ## Imaginary Numbers
>
> Imaginary numbers are numbers that, when squared, have a negative result. The imaginary unit \( i \) is defined as \( \sqrt{-1} \). Imaginary numbers are then numbers that can be written as \( a + bi \), where \( a \) and \( b \) are real numbers and \( i \) is the imaginary unit. Complex numbers are a broader category that includes both real and imaginary numbers and can also be written in the form \( a + bi \).
>
> ### Uses of Imaginary Numbers
>
> 1.  **Electrical Engineering:** Imaginary numbers are used to represent alternating current and voltage in electrical engineering. They make it easier to analyze and understand electrical systems.
>
> 2.  **Control Theory:** In systems and control theory, the use of complex numbers and imaginary units is standard for analyzing system stability.
>
> 3.  **Quantum Mechanics:** Complex numbers, including imaginary numbers, are used to describe the state of quantum systems.
>
> 4.  **Signal Processing:** The Fourier Transform, a cornerstone of signal processing, uses imaginary numbers to transform a signal into its constituent frequencies.
>
> 5.  **Fluid Dynamics:** Complex analysis methods are used in potential flow theory, a subfield of fluid dynamics.
>
> 6.  **Economics:** In some cases, complex numbers have been used to model certain economic conditions or markets.
>
> 7.  **Mathematics:** Imaginary numbers are used in various areas of mathematics, including number theory and certain kinds of equations that cannot be solved using only real numbers.
>
> 8.  **Computer Graphics:** They can be used to perform rotations in 2D space.
>
> 9.  **Data Science:** Techniques like Singular Value Decomposition in machine learning can involve complex numbers, although the imaginary parts are usually discarded in the end.
>
> 10. **Telecommunications:** In designing and understanding systems like radio transmission, imaginary numbers can play a crucial role.
>
> So, even though imaginary numbers may sound "imaginary" or unrealistic, they have a wide range of very practical applications.

Here are some examples of complex numbers used in
python:

```python
>>> print(complex(10, 20))
(10+20j)
>>> print(complex(2.5, -18.2))
(2.5-18.2j)
>>> complex_1 = complex(0, 2)
>>> complex_2 = complex(2, 0)
>>> print(complex_1)
2j
>>> print(complex_2)
(2+0j)
```

Complex numbers are usually denoted as `i` in mathematics, but in Python, we use `j` to represent the imaginary part of the complex number, following the electrical en
gineering convention.

### Booleans

    The Boolean (also known as bool) data type allows us to choose between two values: true and false.

```python
>>> print(True)
True
>>> f_bool = False
>>> print(f_bool)
False
>>> type(f_bool)
<class 'bool'>
```

### Strings

Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string `"hello'` to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

```python
>>> newString = "Wanda"
>>> print(newString[0])
W
>>> print(newString[-1])
a
```

```python
batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]

```

#### Length of a String

We can check the length of a string using the `len()` function.

```python
>>> len(newString)
5
```

#### string immutability

Strings are immutable, which means you cannot change an existing string. The best you can do is create a new string from the existing one.

```python
>>> subString = newString[1:3]
>>> print(subString)
an
```

You can't reassign a letter in string. You have to make a new variable.

Assigning a new value to a string variable will overwrite the previous value. The identity will change but not the value.

```python
>>> print(id(str1))
4334439920
>>> str1 = "bye"
>>> print(id(str1))
4334439984
>>>
```

### ASCII vs. Unicode

In Python3, all strings are sequences of Unicode characters. Unicode is a standard that defines a unique number for an **abstract** character. It is an international encoding standard for use with different languages and scripts, by which each letter, digit, or symbol is assigned a unique numeric value that applies across different platforms and programs.

### # String Slicing

Slicing is the process of obtaining a portion of a string by using it's indices.

You can slice with two indices, separated by a colon. The first index is the start index, and the second index is the end index. The end index is not included in the slice.

You can also slice with a step, which specifies how many characters you want to move forward after the first character is retrieved from the string.

Here's the syntax: `string[start:end:step]`

```python
>>> str1 = "Hello World"
>>> str1[0:5]
'Hello'
>>> str1[6:]
'World'
>>> str1[0:5:2]
'Hlo'
>>> str1[0:5:3]
'Hl'
>>> str1[0:5:4]
'Ho'
>>> str1[0:5:5]
'H'
>>> str1[0:5:6]
'H'
```

Essentially, you define when you start, stop and how many elements you skip. This also works for lists, too.

```python
# Start from index 0, stop at index 12, and step by 2
sliced_string = my_string[0:12:2]
print(sliced_string)  # Output: "Hlo ol"

```

Reversing a string using slicing

```python
my_string = "Hello, World!"
reversed_string = my_string[::-1]
print(reversed_string)  # Output: "!dlroW ,olleH"
```

#### Partial Slicing

```python
>>> my_string = "What the heck is going on here!?"
>>> print(my_string[:8])
What the
>>> print(my_string[8:])
 heck is going on here!?
>>> print(my_string[:])
What the heck is going on here!?
>>> print(my_string[::-1])
?!ereh no gniog si kceh eht tahW
```

## Python Operators

### Arithmetic Operators

![Alt text](image.png)

#### Addition

```python
print(10 + 5)

float1 = 13.65
float2 = 3.40
print(float1 + float2)

num = 20
flt = 10.5
print(num + flt)

```

#### Subtraction

```python
>>> print(10 - 5)
5
>>>
>>> float1 = -18.678
>>> float2 = 3.55
>>> print(float1 - float2)
-22.228
>>>
>>> num = 20
>>> flt = 10.5
>>> print(num - flt)
9.5
```

#### Multiplication

```python
>>> print(40 * 10)
400
>>>
>>> float1 = 5.5
>>> float2 = 4.5
>>> print(float1 * float2)
24.75
>>>
>>> print(10.2 * 3)
30.599999999999998
```

#### Division

```python
>>> print(40 / 10)
4.0
>>>
>>> float1 = 5.5
>>> float2 = 4.5
>>> print(float1 / float2)
1.2222222222222223
>>> print(12.4 / 2)
6.2
```

A division operation always results in a float.

#### Floor Division

In floor division, the result is floored to the nearest smaller integer. It is also known as integer division.

```python
>>> print(43 // 10)
4
>>>
>>> float1 = 5.5
>>> float2 = 4.5
>>> print(5.5 // 4.5)
1.0
>>> print(12.4 // 2)
6.0
```

Unlike normal division, floor division between two integers results in an integer.

#### Modulus

In computing, the modulo operation returns the remainder or signed remainder of a division, after one number is divided by another (called the modulus of the operation).

A number’s modulo with another number can be found using the % operator:

```python
>>> print(10 % 2)
0
>>>
>>> twenty_eight = 28
>>> print(twenty_eight % 10)
8
>>>
>>> print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
2
>>> print(28 % -10)  # The remainder is negative if the right-hand operand is negative
-2
>>> print(34.4 % 2.5)  # The remainder can be a float
1.8999999999999986

```

#### Precedence of Arithmetic Operators

The precedence of arithmetic operators is as follows:

1. Parentheses
2. Exponentiation
3. Multiplication, Division, Floor Division, and Modulus
4. Addition and Subtraction

```python
>>> # Different precedence
>>> print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction
4
>>>
>>> # Same precedence
>>> print(3 * 20 / 5)  # Multiplication computed first, followed by division
12.0
>>> print(3 / 20 * 5)  # Division computed first, followed by multiplication
0.75
>>>
```

Whenever operators have equal precedence, the expression is computed from the left side.

#### Parentheses

```python
>>> print((10 - 3) * 2)  # Subtraction occurs first
14
>>> print((18 + 2) / (10 % 8))
10.0
```

### Comparison Operators

![Alt text](image-1.png)

### Assignment Operators

![Alt text](image-2.png)

Variables a mutable, so they can be changed.

#### Other operators

```python
>>> num = 10
>>> print(num)
10
>>>
>>> num += 5
>>> print(num)
15
>>>
>>> num -= 5
>>> print(num)
10
>>>
>>> num *= 2
>>> print(num)
20
>>>
num /= 2
print(num)

num **= 2
print(num)>>> num /= 2
>>> print(num)
10.0
>>>
>>> num **= 2
>>> print(num)
100.0
```

#### Bit Value

True is 1 and False is 0.

```python
>>> print(10 * True)
10
>>> print(10 * False)
0
```

#### Logical Operators

![Alt text](image-3.png)

```python
>>> # OR Expression
>>> my_bool = True or False
>>> print(my_bool)
True
>>>
>>> # AND Expression
>>> my_bool = True and False
>>> print(my_bool)
False
>>>
>>> # NOT expression
>>> my_bool = False
>>> print(not my_bool)
True
```

#### Bitwise Operators

In programming, all data is actually made up of 0s and 1s known as bits. Bitwise operators allow us to perform bit-related operations on values.

We should probably come back to this later.

![Alt text](image-4.png)

```python
>>> num1 = 10  # Binary value = 01010
>>> num2 = 20  # Binary Value = 10100
>>>
>>> print(num1 & num2)   # 0   -> Binary value = 00000
0
>>> print(num1 | num2)   # 30  -> Binary value = 11110
30
>>> print(num1 ^ num2)   # 30  -> Binary value = 11110
30
>>> print(~num1)         # -11 -> Binary value = -(1011)
-11
>>> print(num1 << 3)     # 80  -> Binary value = 0101 0000
80
>>> print(num2 >> 3)     # 2   -> Binary value = 0010
2
```

### String Operators

#### Comparison

```python
>>> print('a' < 'b')  # 'a' has a smaller Unicode value
True
>>>
>>> house = "Gryffindor"
>>> house_copy = "Gryffindor"
>>>
>>> print(house == house_copy)
True
>>>
>>> new_house = "Slytherin"
>>>
>>> print(house == new_house)
False
>>>
>>> print(new_house <= house)
False
>>>
>>> print(new_house >= house)
True
```

#### Concatenation

```python
>>> first_half = "Bat"
>>> second_half = "man"
>>>
>>> full_name = first_half + second_half
>>> print(full_name)
Batman
```

#### Repetition

```python
>>> print("ha" * 3)
hahaha
```

#### Search

```python
>>> random_string = "This is a random string"
>>>
>>> print('of' in random_string)  # Check whether 'of' exists in randomString
False
>>> print('random' in random_string)  # 'random' exists!
True
```

### Grouping Values

#### Lists

You can use lists to group values of different types together.

```python
>>> my_list = [1, 2.5, "A string", True]
>>> print(my_list[2])
A string
>>> print(len(my_list))
4
```

## Conditional Statements

```python
if condtional statement is True:
    # execute expression1
    pass
else:
    # execute expression2
    pass

```

There are three types of conditional statements in Python:

    if
    if-else

    if-elif-else

### if

```python
>>> num = 5
>>>
>>> if (num == 5):  # The condition is true
...     print("The number is equal to 5")  # The code is executed
...
The number is equal to 5
>>> if num > 5:  # The condtion is false
...     print("The number is greater than 5")  # The code is not executed
...
>>>
```

### if with logical operators

```python
num = 12

if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    # Only works when num is a multiple of 2, 3, and 4
    print("The number is a multiple of 2, 3, and 4")

if (num % 5 == 0 or num % 6 == 0):
    # Only works when num is either a multiple of 5 or 6
    print("The number is a multiple of 5 and/or 6")
```

You can also nest if statements.

```python
>>> if num >= 0 and num <= 100:
...     if num >= 50 and num <= 75:
...         if num >= 60 and num <= 70:
...             print("The number is in the 60-70 range")
...
The number is in the 60-70 range
```

Creating and editing values:

```python
>>> num = 10
>>> if num > 5:
...     num = 20  # Assigning a new value to num
...     new_num = num * 5  # Creating a new value called newNum
...
>>> # The if condition ends, but the changes made inside it remain
>>> print(num)
20
>>> print(new_num)
100
```

### if-else

```python
>>> if num <= 50:
...     print("The number is less than or equal to 50")
... else:
...     print("The number is greater than 50")
...
The number is greater than 50
```

You don't have to restate a condition if the first is false.

#### Conditional Expressions

Conditional expressions use the functionality of an if-else statement in a different way.

The expression returns an output based on the condition we provide. This output can be stored in a variable.

A conditional expression can be written in the following way:

```python
output_value1 if condition else output_value2
```

```python
>>> num = 60
>>>
>>> output = "The number is less than or equal to 50" \
...     if num <= 50 else "The number is greater than 50"
>>>
>>> print(output)
The number is greater than 50
```

    Please note that the backslash \ in the above code is only a line continuation character that can be used to split a single line into multiple lines.

### if-elif-else

```python
light = "Yellow"

if light == "Green":
    print("Go")

elif light == "Yellow":
    print("Caution")

elif light == "Red":
    print("Stop")

else:
    print("Incorrect light signal")

```

Note: An if-elif statement can exist on its own without an else block at the end. However, an elif cannot exist without an if statement preceding it (which naturally makes sense).

```python
>>> num = 5
>>>
>>> if num == 0:
...     print("Zero")
... elif num == 1:
...     print("One")
... elif num == 2:
...     print("Two")
... elif num == 3:
...     print("Three")
... elif num == 4:
...     print("Four")
... elif num == 5:
...     print("Five")
... elif num == 6:
...     print("Six")
... elif num == 7:
...     print("Seven")
... elif num == 8:
...     print("Eight")
... elif num == 9:
...     print("Nine")
...
Five
```

An important thing to keep in mind is that an if-elif-else or if-elif statement is not the same as multiple if statements. if statements act independently.

If the conditions of two successive ifs are True, both statements will be executed.

On the other hand, in if-elif-else, when a condition evaluates to True, the rest of the statement’s conditions are not evaluated.

# Functions

Why Use Functions?

Think of a function as a box which performs a task. We give it an input and it returns an output.

We don’t need to write the set of instructions again for a different input, we could just call the function again.

Functions are useful because they make the code concise and simple. The primary benefits of using functions are:

    Reusability: A function can be used over and over again. You do not have to write redundant code. For example, a sum() function could compute the sum of all the integers we provide it. We won’t have to write the summing operation ourselves each time.

    Simplicity: Functions are easy to use and make the code readable. We only need to know the inputs and the purpose of the function without focusing on the inner workings. This abstraction allows us to focus more on gaining the output instead of figuring out how it was computed.

An input isn’t even necessary. A function could perform its own computations to complete a task.

## Types of Functions in Python

Functions are perhaps the most commonly used feature of Python. There are two basic types of functions in Python:

    Built-in functions
    User-defined functions

len(), min(), and print() are examples of built-in functions.

The coolest feature, however, is that the language allows us to create our own functions that perform the tasks we require.

## The return Statement

So far, we’ve only defined functions that print something. They don’t return anything back to us. But if we think back, functions return values all the time. Just take len() for example. It returns an integer which is the length of the data structure.

To return something from a function, we must use the return keyword. Keep in mind that once the return statement is executed, the compiler ends the function. Any remaining lines of code after the return statement will not be executed.

## Function Scope

The scope of a function means the extent to which the variables and other data items made inside the function are accessible in code.

In Python, the function scope is the function’s body.

Whenever a function runs, the program moves into the function scope. It moves back to the outer scope once the function has ended.
Data Lifecycle

In Python, data created inside the function cannot be used from the outside unless it is being returned from the function.

Variables in a function are isolated from the rest of the program. When the function ends, they are released from memory and cannot be recovered.

```python
>>> name = "Ned"
>>>
>>>
>>> def func():
...     name = "Stark"
...
>>>
>>> func()
>>> print(name)  # The value of 'name' remains unchanged.
Ned
```

Note that a function can access variables from the outer scope. However, it cannot modify them unless they are passed as arguments.

# Scoping differences between Python and JavaScript

### JavaScript

1. **Block Scoping with `let` and `const`:** With ES6, JavaScript introduced `let` and `const`, which are block-scoped.
2. **Function Scoping with `var`:** Before ES6, we had only `var`, which is function-scoped.
3. **Hoisting:** In JavaScript, variable and function declarations are hoisted to the top of their containing function or block, but the initializations are not.
4. **Nested Functions:** Functions can be nested within other functions, and inner functions have access to the variables in the outer functions, creating closures.
5. **Global Scope:** Variables defined outside any function or block are in the global scope, and they can be accessed from any part of the code, including functions.
6. **`this` Keyword:** JavaScript functions have a `this` keyword which can differ depending on how the function is called (e.g., as a method, regular function, arrow function, etc.).

Example:

```javascript
function outer() {
  let a = 10;
  var b = 20;

  function inner() {
    let c = 30;
    console.log(a); // Accessible
    console.log(b); // Accessible
  }

  console.log(c); // Error
}
```

### Python

1. **Function-level Scoping:** Python doesn't have block-level scoping for variables. A variable declared within a function is only available within that function.
2. **No Hoisting:** Variables in Python are not hoisted. You have to declare a variable before you use it.
3. **Nested Functions:** Like JavaScript, Python allows nested functions, and inner functions can access outer function variables.
4. **Global and Nonlocal Keywords:** Python uses `global` and `nonlocal` keywords to refer to a variable in the global or outer function scope respectively.
5. **Built-in Scope:** Python has a built-in scope, which includes built-in functions like `len()` and `abs()`.
6. **`self` Parameter:** In Python, instance methods in classes need to take a `self` parameter to refer to the instance of the class, somewhat similar to `this` in JavaScript but more explicit.

Example:

```python
def outer():
    a = 10

    def inner():
        nonlocal a
        a += 20
        print(a)  # Accessible and will print 30

    inner()
    print(a)  # Will print 30

outer()
```

### Summary

- JavaScript has block-level scoping with `let` and `const` and function-level scoping with `var`.
- Python has function-level scoping by default.
- Both languages allow nested functions and closures.
- Hoisting is unique to JavaScript.
- Python requires `global` or `nonlocal` to change variables in outer scopes, while JavaScript uses `var`, `let`, or `const`.

Given your background, grasping these distinctions will help you switch gears between front-end development and Python more efficiently.

Note that this will print 30 twice. This is because the `nonlocal` keyword allows us to modify the variable in the outer scope.

```python
def outer():
    a = 10

    def inner():
        nonlocal a  # tell Python that a is not local to inner, but is in the nearest outer scope
        a += 20
        print(a)  # Will print 30

    inner()
    print(a)  # Will also print 30

outer()

```

While this will print 30 and 10:

```python
def outer():
    a = 10

    def inner(a):
        a += 20
        print(a)  # will print 30

    inner(a)
    print(a)  # Will print 10

outer()

```

See how the num_list has been changed since it was called as an argument.

```python
>>> num_list = [10, 20, 30, 40]
>>> print(num_list)
[10, 20, 30, 40]
>>>
>>>
>>> def multiply_by_10(my_list):
...     my_list[0] *= 10
...     my_list[1] *= 10
...     my_list[2] *= 10
...     my_list[3] *= 10
...
>>>
>>> multiply_by_10(num_list)
>>> print(num_list)  # The contents of the list have been changed
[100, 200, 300, 400]
```

## String Methods

### String Methods

Strings are objects in Python. This means that they have certain properties and methods that we can use to perform operations on them.

A method is a function that belongs to an object. It is called using the dot notation.

```python
>>> my_string = "Hello World"
>>> print(my_string.upper())
HELLO WORLD
>>> print(my_string.lower())
hello world
>>> print(my_string.title())
Hello World
>>> print(my_string.count("l"))
3
>>> print(my_string.count("o"))
2
>>> print(my_string.count(" "))
1
>>> print(my_string.count("Hello"))
1
>>> print(my_string.count("hello"))
0
>>> print(my_string.count("llo"))
1
>>> print(my_string.count("ll"))
1
>>> print(my_string.count("lll"))
0
```

See built in String methods

```

```

## Lambdas

Lambda functions are anonymous functions. They are functions that are defined without a name.

```python
>>> triple = lambda num : num * 3  # Assigning the lambda to a variable
>>>
>>> print(triple(10))  # Calling the lambda and giving it a paramete
30

>>> triple = lambda num : num * 3  # Assigning the lambda to a variable
>>>
>>> print(triple(10))  # Calling the lambda and giving it a paramete
30
>>> concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
>>>
>>> print(concat_strings("World", "Wide", "Web"))
WWW
```

A lambda cannot have a multi-line expression. This means that our expression needs to be something that can be written in a single line.

They are perfect for one line conditional statements.

```python

```

> > > my_func = lambda num: "High" if num > 50 else "Low"
> > > my_func(20)
> > > 'Low'
> > > my_func(60)
> > > 'High'

```

Lambdas are really useful when a function requires another function as its argument.
```

```python
def factorial(n):
    i

```

## Loops

Definition

    A loop is a control structure that is used to perform a set of instructions for a specific number of times.

Loops solve the problem of having to write the same set of instructions over and over again. We can specify the number of times we want the code to execute.

One of the biggest applications of loops is traversing data structures, e.g. lists, tuples, sets, etc. In such a case, the loop iterates over the elements of the data structure while performing a set of operations each time.

Just like conditional statements, a loop is classified as a control structure because it directs the flow of a program by making varying decisions in its iterations.

Loops are a crucial part of many popular programming languages such as C++, Java, and JavaScript.

### While Loops

The while loop keeps iterating over a certain set of operations as long as a certain condition holds True.

It operates using the following logic:

While this condition is true, keep the loop running.

Watch out for  infinite loops.




```python
>>> num = 0
>>>
>>> while num < 10:
...     print(num)
...     num += 1
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

### For Loops

The range function is a built-in function in Python that generates a sequence of numbers. It is commonly used in for loops.

```python
range(start, end, step)
```

```python
>>> for num in range(10):
...     print(num)
...
0
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

Here's a for loop using the range

```python
>>> for i in range(1, 11):  # A sequence from 1 to 10
...     if i % 2 == 0:
...         print(i, " is even")
...     else:
...         print(i, " is odd")
...
1  is odd
2  is even
3  is odd
4  is even
5  is odd
6  is even
7  is odd
8  is even
9  is odd
10  is even
>>>
```

Iterate between the first index and the last index in a list using the length of the list.

```python
>>> float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
>>> print(float_list)
[2.5, 16.42, 10.77, 8.3, 34.21]
>>>
>>> for i in range(0, len(float_list)):  # Iterator traverses to the last index of the list
...     float_list[i] = float_list[i] * 2
...
>>> print(float_list)
[5.0, 32.84, 21.54, 16.6, 68.42]
```

Here we use the range function to skip every third number.

```python
>>> for i in range(1, 11, 3):  # A sequence from 1 to 10 with a step of 3
...     print(i)
...
1
4
7
10
```

## Nested Loops

### Execution of Nested Loops

Python lets us easily create loops within loops. There’s only one catch: the inner loop will always complete before the outer loop.

For each iteration of the outer loop, the iterator in the inner loop will complete its iterations for the given range, after which the outer loop can move to the next iteration.

Here's an example of a nested loop

```python
>>> n = 50
>>> num_list = [10, 25, 4, 23, 6, 18, 27, 47]
>>>
>>> for n1 in num_list:
...     for n2 in num_list:  # Now we have two iterators
...         if(n1 != n2):
...             if(n1 + n2 == n):
...                 print(n1, n2)
...
23 27
27 23
```

Each element is compared with every other element to check if n1 + n2 is equal to n.

## Loop Control Statements

### Break

The break statement is used to terminate a loop. It is used to break out of a loop when a certain condition is met.

```python
>>> for n1 in num_list:
...     for n2 in num_list:
...         if(n1 != n2):
...             if(n1 + n2 == n):
...                 found = True  # Set found to True
...                 break  # Break inner loop if a pair is found
...     if found:
...         print(n1, n2) # Print the pair
...         break  # Break outer loop if a pair is found
...
23 27
```


### Continue

The continue statement is used to skip the current iteration of a loop. It is used to skip over a part of a loop when a certain condition is met.



### The pass Keyword

In all practical meaning, the `pass` statement does nothing to the code execution. It can be used to represent an area of code that needs to be written. Hence, it is simply there to assist you when you haven’t written a piece of code but still need your entire program to execute.