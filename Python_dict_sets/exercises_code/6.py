def toggle(flag, element: set):
    if flag in element:
        element.discard(flag)
    else:
        element.add(flag)


def toggled(flag, element: set):
    result = element.copy()
    toggle(flag, result)

    return result


def main():
    READ_ONLY = 'read_only'
    flags = set()
    toggle(READ_ONLY, flags)
    print(READ_ONLY in flags)
    toggle(READ_ONLY, flags)
    print(READ_ONLY in flags)
    print()
    print()


if __name__ == '__main__':
    main()
