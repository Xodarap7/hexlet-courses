from itertools import cycle


def round_robin(*args):
    sources = [
        (index, iter(source))
        for index, source in enumerate(args)
    ]

    rest_sources = {index for index, _ in sources}
    for index, source in cycle(sources):
        if index in rest_sources:
            for next_value in source:
                yield next_value
                break
            else:
                rest_sources.remove(index)
        if not rest_sources:
            break


def main():
    print(list(round_robin("ab", "QWE")))
    # print(list(round_robin()))
    print()


if __name__ == '__main__':
    main()
