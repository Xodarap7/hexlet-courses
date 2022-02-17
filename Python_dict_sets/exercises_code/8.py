def apply_diff(target: set, dictionary: dict):
    if 'add' in dictionary:
        target.update(dictionary['add'])
    if 'remove' in dictionary:
        target.difference_update(dictionary['remove'])


def apply_diff_example(set_for_update, diff):
    """hexlet example"""

    set_for_update.update(diff.get('add', {}))
    set_for_update.difference_update(diff.get('remove', {}))


def main():
    target = {'a', 'b'}
    diff = {'add': {'c'}, 'remove': {'a'}}
    apply_diff(target, diff)
    print(target)
    apply_diff(target, {})
    print()
    print()


if __name__ == '__main__':
    main()
