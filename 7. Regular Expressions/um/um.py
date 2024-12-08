import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    words = s.split()
    counter = 0
    for word in words:
        if matches := re.findall(r"^um[^\w]*$", word, re.IGNORECASE):
            counter += 1
    return counter

if __name__ == "__main__":
    main()
