def number_of_unique_letters(element: str) -> int:
    set_ = {char for char in element.lower() if char.isalpha()}

    return len(set_)


def main():
    print(number_of_unique_letters("A-a-a-a-a-a!"))
    print(number_of_unique_letters(""))
    print(number_of_unique_letters("AaBbCcDd"))


if __name__ == '__main__':
    main()
