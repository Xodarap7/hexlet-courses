def diff_keys(old, new) -> dict:
    dictionary = {
        'kept': set(old) & set(new),
        'added': set(new) - set(old),
        'removed': set(old) - set(new)
    }

    return dictionary


def main():
    print(diff_keys({'name': 'Bob', 'age': 42}, {}))
    print(diff_keys({}, {'name': 'Bob', 'age': 42}))
    print(diff_keys({'a': 2}, {'a': 1}))


if __name__ == '__main__':
    main()
