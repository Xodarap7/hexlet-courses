from typing import List, Any


def my_map(function, original_list: List[Any]):
    for item in original_list:
        yield function(item)


def my_filter(function, original_list: List[Any]):
    for item in original_list:
        if function(item):
            yield item


def replicate_each(n, original_list: List[Any]):
    for item in original_list:
        i = n
        while i > 0:
            yield item
            i -= 1


def main():
    print(list(my_map(abs, [-1, 2, -3])))
    print()
    print(list(my_filter(lambda x: x % 2 == 1, range(10))))
    print()
    print(list(replicate_each(1, [1, 'a'])))
    print(list(replicate_each(3, [1, 'a'])))
    print(list(replicate_each(0, [1, 'a'])))


if __name__ == '__main__':
    main()
