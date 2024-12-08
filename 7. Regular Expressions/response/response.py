from validator_collection import validators, checkers, errors


def main():
    print(validate(input("What's your email adress? ")))


def validate(s):
    is_email_address = checkers.is_email(s)
    if is_email_address:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
