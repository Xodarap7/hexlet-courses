from typing import List, Any

LIST_ITEMS = List[Any]


def is_int(x):
    return isinstance(x, int)


def each2d(test, matrix: List[LIST_ITEMS]) -> bool:
    return all(all(test(item) for item in element)for element in matrix)


def some2d(test, matrix):
    return any(any(test(item) for item in element)for element in matrix)


def sum2d(test, matrix):
    return sum(sum(item for item in element if test(item))for element in matrix)


def main():
    print(each2d(is_int, [[1, 2], [3, 4]]))
    print(each2d(is_int, [[1, None], [3, 4]]))
    print(each2d(is_int, []))
    print()
    print(some2d(is_int, [[None, "foo"], [(), {}]]))
    print(some2d(is_int, [[None, "foo"], [0, {}]]))
    print(some2d(is_int, []))
    print()
    print(sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]))


if __name__ == '__main__':
    main()
