# This is pyPassword generator
import random


def main():
    print("Welcome to pyPassword Generator!")
    no_of_letters = int(input("How many letters would you like in your password? \n"))
    no_of_symbols = int(input("How many symbols would you like?\n"))
    no_of_digits = int(input("How many numbers would you like? \n"))

    password = generate_password(no_of_symbols, no_of_letters, no_of_digits)
    print("Here is your password:", password)


def generate_password(s, l, d):
    symbols = ['!', '@', '$', '%', '^', '&', '*', '(', ')', '~', '`', ':', '<', '>', '?', '"', '.', '/', '[', ']',
               '{', '}']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    p_symbols = random.choices(symbols, k=s)
    p_letters = random.choices(letters, k=l)
    p_digits = list(map(str, random.choices(range(0, 10), k=d)))

    p = p_digits + p_letters + p_symbols
    random.shuffle(p)
    password = "".join(p)

    return password


if __name__ == '__main__':
    main()