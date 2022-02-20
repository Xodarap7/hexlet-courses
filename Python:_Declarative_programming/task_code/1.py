from typing import TypeVar, Iterable, Any


# def intersperse(source, separator):
#     cursor = iter(source)
#     for first_item in cursor:
#         yield first_item
#         break
#     for next_item in cursor:
#         yield separator
#         yield next_item


def intersperse(iterator: Iterable, separator: Any) -> Iterable:
    for i, item in enumerate(iterator):
        if i == 0:
            yield item
        else:
            yield separator
            yield item


def main():
    print(list(intersperse(range(4), 0)))
    print("".join(intersperse(["Hello", "World"], " ")))
    print(list(intersperse([42], "foo")))
    print(list(intersperse([], ",")))


if __name__ == '__main__':
    main()
