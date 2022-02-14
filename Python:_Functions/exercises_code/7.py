from functools import reduce
from operator import getitem


def keep_truthful(source: iter) -> list:

    return list(filter(None, source))


def abs_sum(source: iter) -> int:

    return sum(list(map(abs, source)))


def walk(dictionary: dict, param: list):

    return reduce(getitem, param, dictionary)


def main():
    print(keep_truthful([True, False, "", "foo"]))
    print(abs_sum([-3, 7]))
    print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"]))


if __name__ == '__main__':
    main()
