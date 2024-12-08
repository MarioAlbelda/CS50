def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


#Validating all functions.
def is_valid(s):
    return start(s) and length(s) and numbers(s)

#Checking if starts with at least two letters.
def start(s):
        return s[:2].isalpha()


#Checking the length is between 2 and 6 characters.
def length(s):
    return 2 <= len(s) <= 6


def numbers(s):
    first_digit_index = len(s)
    for i in s:
        if not i.isalpha():
            first_digit_index = s.index(i)
            break

    if first_digit_index == len(s):
        return True

    return s[first_digit_index:].isdigit() and s[first_digit_index] != "0"

if __name__ == "__main__":
    main()
