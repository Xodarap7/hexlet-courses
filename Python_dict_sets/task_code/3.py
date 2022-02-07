# 3rd task code

DICTIONARY = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}


def to_arabic(number):  # noqa: WPS210
    numbers = []

    for char in number:
        numbers.append(DICTIONARY[char])

    shifted_numbers = numbers[1:] + numbers[-1:]
    result = 0

    for previous, current in zip(numbers, shifted_numbers):

        if previous >= current:
            result += previous
        else:
            result -= previous
        print(result)
    if to_roman(result) != number:
        return False

    return result


def to_roman(number: int) -> str:
    values = sorted(DICTIONARY.values())
    keys = list(DICTIONARY.keys())
    result = ''

    while number > 0:
        if number >= 1000:
            result += 'M'
            number = number - 1000

        else:
            index = 0
            for index, value in enumerate(values):
                if value > number:
                    result += f'{keys[index-1]}'
                    number = number - values[index-1]
                    index += 1
                    break

    return result


def main():
    print(to_roman(1))
    print(to_roman(3000))
    print(to_arabic('CMXI'))


if __name__ == '__main__':
    main()
