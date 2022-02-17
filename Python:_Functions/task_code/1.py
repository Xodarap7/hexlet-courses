# from datetime import date

USERS = [
    {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
    {'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
    {'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
    {'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
    {'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
    {'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
    {'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
    {'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
]


def get_men_counted_by_year(list_of_user: list) -> dict:
    birthdays = []
    result = {}

    for user in list_of_user:
        birthdays.append(user['birthday'][:4])

    for birthday in birthdays:
        result[int(birthday)] = birthdays.count(birthday)

    return result


def main():

    print(get_men_counted_by_year(USERS))
    print()
    print()


if __name__ == '__main__':
    main()
