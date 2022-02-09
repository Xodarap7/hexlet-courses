def rgb2hex(r=0, g=0, b=0):
    red = hex(r)[2:].rjust(2, '0')
    green = hex(g)[2:].rjust(2, '0')
    blue = hex(b)[2:].rjust(2, '0')

    return '#{}{}{}'.format(red, green, blue)


def hex2rgb(hex:str):

    return dict(
        r=int(hex[1:3], 16),
        g=int(hex[3:5], 16),
        b=int(hex[5:], 16)
    )


def main():
    print(rgb2hex(0, 132, 12))
    print(rgb2hex(36, 171, 0))
    print(rgb2hex(0, 0, 0))
    print(rgb2hex(r=36, g=171, b=0))
    print(hex2rgb('#24ab00'))


if __name__ == '__main__':
    main()
