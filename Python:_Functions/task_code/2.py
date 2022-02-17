def compose(function2, function1):
    def inner(x):

        return function2(function1(x))

    return inner


def add5(x):
    return x + 5


def mul3(x):
    return x * 3


def main():

    print(compose(mul3, add5)(1))
    print(compose(mul3, str)(1))
    print()


if __name__ == '__main__':
    main()
