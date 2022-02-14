a = 5


def test():
    b = 47

    def test2():
        nonlocal b
        print(a, b)
    return test2

f=test()
f()
