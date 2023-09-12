def outer():
    a = 10

    def inner(a):
        a += 20
        print(a)  # will print 30
        return a

    inner(a)
    print(a)  # Will print 10


outer()
