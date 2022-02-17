from typing import List, Any

LIST_ITEMS = List[Any]
LIST_NUMBERS = List[int]


def non_empty_truths(elements: List[LIST_ITEMS]) -> List[LIST_ITEMS]:

    return [new_element for new_element in [[item for item in element if item] for element in elements] if new_element]


def main():
    print(non_empty_truths([]))
    print(non_empty_truths([[], []]))
    print(non_empty_truths([[0]]))
    print(non_empty_truths([[0, 1, 2], [], [], [False, True, 42]]))
    print()


if __name__ == '__main__':
    main()
