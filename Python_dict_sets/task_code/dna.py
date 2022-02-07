# 1st task code

DNA_TO_RNA_TEMPLATE = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_str: str) -> str:
    result = ''
    for element in dna_str:
        result += DNA_TO_RNA_TEMPLATE[element]

    return result


def main():
    print(to_rna('ACGTGGTCTTAA'))
    print()
    print()


if __name__ == '__main__':
    main()
