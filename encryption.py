import random
import argparse

def main():
    parser = argparse.ArgumentParser(description='Take plaintext and encrypt to cyphertext')
    parser.add_argument('filename', help='A text file must be input here for the encryption algorithm to read')
    cmdline = parser.parse_args()

    with open(cmdline.filename) as f:
        key_space = {}
        initial_numbers = []
        initial_letters = []
        cyphertext = ""

        for i in range(0, 106):
            initial_numbers.append(i)

        initial_letters.extend(["b", "j", "k", "q", "v", "x", "z"])

        for i in range(0, 2):
            initial_letters.extend(["c", "f", "g", "m", "p", "u", "w", "y"])

        for i in range(0, 3):
            initial_letters.append("l")

        for i in range(0, 4):
            initial_letters.append("d")

        for i in range(0, 5):
            initial_letters.extend(["h", "r", "s"])

        for i in range(0, 6):
            initial_letters.extend(["i", "n", "o"])

        for i in range(0, 7):
            initial_letters.extend(["a", "t"])

        for i in range(0, 10):
            initial_letters.append("e")

        for i in range(0, 19):
            initial_letters.append(" ")

        for i in range(105, -1, -1):
            letter = initial_letters.pop(random.randint(0, i))
            number = initial_numbers.pop(random.randint(0, i))
            key_space.setdefault(letter, []).append(number)

        print(key_space)

        for line in f:
            for char in line:
                size_key = len(key_space[char]) - 1
                cyphertext = cyphertext + str(key_space[char][random.randint(0, size_key)]) + ","

        cyphertext = cyphertext[:-1]
        print(cyphertext)


if __name__ == "__main__":
    main()