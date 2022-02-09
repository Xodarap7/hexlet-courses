from functools import reduce

POWERS_OF_TWO = (2 ** 24, 2 ** 16, 2 ** 8, 2 ** 0)  # noqa: WPS221


# def ip2int(ip: str):
#     ip = ip.split('.')
#     result = int(ip[0]) * 16777216 + int(ip[1]) * 65536 + int(ip[2]) * 256 + int(ip[3])
#     return result


def ip2int(ip):
    return sum(map(
        lambda x, y: int(x) * y,
        ip.split('.'),
        POWERS_OF_TWO,
    ))


def _make_octet(accumulator, divider):
    ip, remainder = accumulator
    octet, new_remainder = divmod(remainder, divider)
    return ip + (str(octet),), new_remainder


def int2ip(integer):
    octets, _ = reduce(_make_octet, POWERS_OF_TWO, ((), integer))
    return '.'.join(octets)


def main():

    print(ip2int('128.32.10.1'))
    print(ip2int('0.0.0.0'))
    print(int2ip(2149583361))
    print(int2ip(0))


if __name__ == '__main__':
    main()
