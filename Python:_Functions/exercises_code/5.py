def call_twice(function, *args, **kwargs):

    result1 = function(*args, **kwargs)
    result2 = function(*args, **kwargs)

    return result1, result2


def push_and_count(target, *, value):
    target.append(target)
    return len(target)


def shoot():
    return 'Bang!'


def main():

    print(call_twice(shoot))
    print(call_twice(push_and_count, [], value=42))
    print()


if __name__ == '__main__':
    main()
