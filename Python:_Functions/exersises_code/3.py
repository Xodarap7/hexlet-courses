def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


def get_colors():
    colors = {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255)
    }

    return colors


def main():
    colors = get_colors()
    print(colors['red'])
    print(colors['blue'])
    print()


if __name__ == '__main__':
    main()
