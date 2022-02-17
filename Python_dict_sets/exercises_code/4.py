def collect_indexes(element) -> dict:
    dictionary = {}
    for i, el in enumerate(element):
        dictionary.setdefault(el, []).append(i)
    return dictionary


def main():
    print(collect_indexes("hello"))
    print()
    print()


if __name__ == '__main__':
    main()
