def updated(dictionary: dict, **kwargs):
    result = dictionary.copy()
    result.update(kwargs)
    return result


def main():
    d = {'a': 1, 'b': False}
    print(updated(d, a=2, b=True, c=None))
    print()
    print()


if __name__ == '__main__':
    main()
