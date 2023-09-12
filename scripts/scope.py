def outer():
    a = 10

    def inner():
        nonlocal a
        a += 20
        print(a)  # Accessible and will print 30

    inner()
    print(a)  # Will print 30

outer()

