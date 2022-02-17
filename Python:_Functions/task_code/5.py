def find_index_of_nearest(desired_number: int, elements: list):
    diff = {}
    desired_value = None

    if elements:
        for index, element in enumerate(elements):
            diff[element] = abs(element-desired_number)

        min_diff = min(diff.values())

        for key, value in diff.items():
            if value == min_diff:
                desired_value = key
                break

        return elements.index(desired_value)


def find_index_of_nearest_example(number, source):
    """
    hexlet example
    """
    if source:
        diff = list(map(lambda x: abs(x - number), source))

        return diff.index(min(diff))


def main():
    print(find_index_of_nearest(0, [15, 10, 3, 4]))
    print(find_index_of_nearest(4, [7, 5, 3, 2]))
    print(find_index_of_nearest(4, [7, 5, 4, 4, 3]))


if __name__ == '__main__':
    main()
