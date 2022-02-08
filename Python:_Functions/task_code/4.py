def decode(element: str) -> str:
    result = ''
    fragments = element.split('|')

    for i, fragment in enumerate(fragments):
        if i == 0:
            result += '0'*len(fragment)
        else:
            result += '1' + '0'*(len(fragment)-1)

    return result


def main():

    print(decode('_|¯|____|¯|__|¯¯¯'))
    print(decode('¯|___|¯¯¯¯¯|___|¯|_|¯'))
    print()


if __name__ == '__main__':
    main()
