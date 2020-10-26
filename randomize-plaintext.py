import random
import argparse

def main():
    parser = argparse.ArgumentParser(description='Take plaintext and encrypt to cyphertext')
    parser.add_argument('filename', help='A text file must be input here for the encryption algorithm to read')
    cmdline = parser.parse_args()

    with open(cmdline.filename) as f:
        plaintext = ""
        all_words = []
        for word in f:
            all_words.append(word.split("\n",1)[0])

        while(len(plaintext) < 500):
            plaintext = plaintext + str(all_words[random.randint(0, len(all_words) - 1)]) + " "

        if (len(plaintext) > 500):
            plaintext = plaintext[:500]

        print(plaintext)

if __name__ == "__main__":
    main()