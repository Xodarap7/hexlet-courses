def partial_apply(function, arg1):

    def inner(arg2):
        return function(arg1, arg2)

    return inner


def flip(function):

    def inner(arg1, arg2):
        return function(arg2, arg1)

    return inner


def greet(name, surname):
    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)


def main():
    f = partial_apply(greet, 'Dorian')
    a = f('Grey')
    print(a)


if __name__ == '__main__':
    main()
