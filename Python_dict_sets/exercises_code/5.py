def all_unique(element) -> bool:
    items = list(element)

    return len(set(items)) == len(element)


def main():
    print(all_unique("cat"))
    print(all_unique([1, 2, 1]))
    print(all_unique([]))


if __name__ == '__main__':
    main()
