def rgb2tuple(rgb):
    if isinstance(rgb, RGB):
        return rgb.red, rgb.green, rgb.blue


class RGB:
    red = 0
    green = 0
    blue = 0


def main():
    red, green, blue = RGB(), RGB(), RGB()
    red.red, green.green, blue.blue = 255, 255, 255

    print(rgb2tuple(42))
    print(rgb2tuple(red))
    print(rgb2tuple(green))


if __name__ == '__main__':
    main()
