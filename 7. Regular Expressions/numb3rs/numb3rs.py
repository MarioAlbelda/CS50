import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        if int(matches.group(1)) > 255:
            return False
        elif int(matches.group(2)) > 255:
            return False
        elif int(matches.group(3)) > 255:
            return False
        elif int(matches.group(4)) > 255:
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
