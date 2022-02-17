from typing import List, Any

LIST_ITEMS = List[Any]
LIST_NUMBERS = List[int]


def odds_from_odds(elements: List[LIST_ITEMS]) -> List[LIST_ITEMS]:
    """
    Function changes the original element
    """
    result = []

    for i, element in enumerate(elements):
        new_element = []

        if (i+1) % 2 == 1:

            for j, number in enumerate(element):
                if (j+1) % 2 == 1:
                    new_element.append(number)
            result.append(new_element)

    return result


def find_to_delete(elem: LIST_ITEMS) -> None:
    """
    Create list of index with elements to delete
    """
    to_delete = []

    for i, _ in enumerate(elem):
        if (i+1) % 2 == 0:
            to_delete.append(i)

    delete_items(to_delete, elem)


def delete_items(to_delete: LIST_NUMBERS, elem: LIST_ITEMS) -> None:
    """
    deleting an element by index
    """
    to_delete.reverse()

    for item in to_delete:
        elem.pop(item)


def keep_odds_from_odds(elements: LIST_ITEMS) -> None:
    """
    Function does not change the original element
    """
    find_to_delete(elements)

    for element in elements:
        find_to_delete(element)


def main():
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]]
    print(odds_from_odds(l))
    print(l)
    print(odds_from_odds([]))
    print(odds_from_odds([[]]))

    print(keep_odds_from_odds(l))
    print(l)
    print(keep_odds_from_odds([]))
    print(keep_odds_from_odds([[]]))


if __name__ == '__main__':
    main()
