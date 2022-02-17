def count_all(element) -> dict:
    dictionary = {}
    for el in element:
        dictionary[el] = element.count(el)
    return dictionary


def main():
    print(count_all(["cat", "dog", "cat"]))
    print(count_all("hello"))
    print()


if __name__ == '__main__':
    main()
