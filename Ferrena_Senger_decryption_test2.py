import argparse
import sys

sys.setrecursionlimit(1500)

def extend_plaintext(plaintext, cypherlist, all_words):
    if (len(plaintext) == 0):
        for word in all_words:
            final_plaintext = extend_plaintext(word + " ", cypherlist, all_words)
            if (len(final_plaintext) == len(cypherlist)):
                return final_plaintext
    else:
        plaintext_flag = True
        keyspace = {}

        if (len(plaintext) > len(cypherlist)):
            plaintext = plaintext[:len(cypherlist)]
        for i in range(0, len(plaintext), 1):
            if (plaintext_flag == False): break
            if not (plaintext[i] in keyspace):
                for j in range(i + 1, len(plaintext), 1):
                    if (cypherlist[j] == cypherlist[i]):
                        keyspace[cypherlist[i]] = plaintext[i]
                        if not (plaintext[j] == plaintext[i]):
                            plaintext_flag = False
                            break

        if (plaintext_flag == True):
            if (len(plaintext) == len(cypherlist)):
                return plaintext
            else:
                for word in all_words:
                    final_plaintext = extend_plaintext(plaintext + word + " ", cypherlist, all_words)
                    if (len(final_plaintext) == len(cypherlist)):
                        return final_plaintext

        return ""


def main():
    parser = argparse.ArgumentParser(description='Take cyphertext and a dictionary to output plaintext')
    parser.add_argument('filename', help='A dictionary is input here for the program to pull from')
    cmdline = parser.parse_args()

    with open(cmdline.filename) as f:
        all_words = []
        for word in f:
            all_words.append(word.split("\n",1)[0])

        cyphertext = input("Please put cyphertext here: ")
        cypherlist = cyphertext.split(",")

        plaintext = extend_plaintext("", cypherlist, all_words)
        print(plaintext)

if __name__ == "__main__":
    main()
