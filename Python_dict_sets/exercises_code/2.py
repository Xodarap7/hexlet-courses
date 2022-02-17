def make_user(name: str, age: int) -> dict:
    return {'name': name, 'age': age}


def format_user(user: dict) -> str:
    return f"{user['name']}, {user['age']}"


def main():
    user = make_user('Phil', 25)
    print(format_user(user))
    print()


if __name__ == '__main__':
    main()
