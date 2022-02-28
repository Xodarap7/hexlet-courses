def rgb(red, green, blue):
    return red, green, blue


class Color:
    red = rgb(255, 0, 0)
    green = rgb(0, 255, 0)
    blue = rgb(0, 0, 255)


def main():
    print(Color.red)
    print(Color.green == rgb(0, 255, 0))
    print()


if __name__ == '__main__':
    main()
