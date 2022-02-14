def filter_map(function, source) -> list:
    result = []

    for element in source:
        resolution, res = function(element)

        if resolution:
            result.append(res)

    return result


def main():

    print()
    print()
    print()


if __name__ == '__main__':
    main()
