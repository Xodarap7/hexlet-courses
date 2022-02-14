def make_module(step=1) -> dict:

    return {
        'inc': lambda x: x + step,
        'dec': lambda x: x - step
    }


def main():
    m = make_module()
    m2 = make_module(step=2)
    print(m['inc'](10))
    print(m['dec'](20))
    print(m2['inc'](1))


if __name__ == '__main__':
    main()
