def greet(name1: str, *args: str) -> str:
    names = []
    for name in (name1,) + args:
        names.append(name)
    result = f'Hello, {" and ".join(names)}!'

    return result


def greet_example(who, *args):
    """
    hexlet example
    """
    names = ' and '.join((who,) + args)
    return 'Hello, {}!'.format(names)


def main():
    print(greet('Moe', 'Mary'))
    print(greet(*'ABC'))
    print()


if __name__ == '__main__':
    main()
