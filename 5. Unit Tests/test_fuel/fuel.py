def main():
    fraction = str(input("Fraction: "))
    print(gauge(convert(fraction)))


def convert(fraction):
    while True:
        try:
            fractionated = fraction.split("/")
            x = int(fractionated[0])
            y = int(fractionated[1])
        except ValueError:
            raise ValueError
        else:
            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                raise ValueError
            else:
                return int(round(x / y * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
