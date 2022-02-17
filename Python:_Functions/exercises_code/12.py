def is_odd(number):
    return False if number == 0 else is_even(number - 1)


def is_even(number):
    return True if number == 0 else is_odd(number - 1)


def main():

    print(is_even(6))
    print(is_even(5))
    print()


if __name__ == '__main__':
    main()
