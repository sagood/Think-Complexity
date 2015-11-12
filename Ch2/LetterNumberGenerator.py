import string


def generate_letters_numbers():
    number = 1
    while True:
        for letter in string.ascii_lowercase:
            yield letter + str(number)
        number += 1


def main(script, *args):
    count = 0
    for letter_number in generate_letters_numbers():
        print(letter_number)
        count += 1
        if count > 100:
            break


if __name__ == '__main__':
    import sys

    main(*sys.argv)
