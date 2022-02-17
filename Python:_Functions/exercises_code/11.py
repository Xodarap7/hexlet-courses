from functools import wraps


def memoizing(arg):
    """
    func
    """
    def wrapper(function):
        """
        Func
        """
        memory = {}
        xes = []

        @wraps(function)
        def inner(x):
            memoized_result = memory.get(x)

            if memoized_result is None:
                xes.append(x)
                memoized_result = function(x)
                memory[x] = memoized_result

                if len(xes) > arg:
                    to_del = xes.pop(0)
                    memory.pop(to_del)

            return memoized_result

        return inner

    return wrapper


@memoizing(2)
def f(x):
    print('Calculating...')

    return x * 10


def main():

    print(f(1))
    print(f(1))
    print(f(2))
    print(f(10))
    print(f(4))
    print(f(1))


if __name__ == '__main__':
    main()
