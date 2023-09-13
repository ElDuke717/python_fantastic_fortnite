# Return the nth term in the Fibonacci sequence without using recursion

# fib(n) determines the nth term in a Fibonacci sequence
def fib(n):
    fib_list = [0, 1]
    # run the fibonacci sequence until reach n
    for i in range(2, n):
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    return fib_list[-1]


nth_term = input(
    "Enter a number to determine the term in the Fibonacci sequence: ")
print(fib(7))


def fib(n):
    # The first and second values will always be fixed
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        return first

    if n == 2:
        return second

    count = 3  # Starting from 3 because we already know the first two values
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1  # Increment count in each iteration
    return fib_n


n = 7
print(fib(n))
