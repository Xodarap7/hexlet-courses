def memoized(function):
    memory = {}

    def inner(x):
        memoized_result = memory.get(x)
        if memoized_result is None:
            memoized_result = function(x)
            memory[x] = memoized_result
        return memoized_result

    return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10


def main():

    print(f(1))
    print(f(1))
    print(f(10))


if __name__ == '__main__':
    main()
