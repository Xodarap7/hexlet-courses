# 2nd task code

EXAMPLE = {
    'G': 10,
    'C': 1,
    'per': 10,
    'page': 123,
    'A': 8340
}


def build_query_string(parameters: dict) -> str:
    parameter_str = []
    parameter_keys = sorted(parameters.keys())

    for key in parameter_keys:
        parameter_str.append(f'{key}={parameters[key]}')

    return '&'.join(parameter_str)


def main():
    print(build_query_string(EXAMPLE))
    print()
    print()


if __name__ == '__main__':
    main()
