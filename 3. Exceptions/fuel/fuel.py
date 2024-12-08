
def main():
    percent = percentage()
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


def percentage():
    while True:
        try:
            fraction = str(input("Fraction: ")).split("/")
            x = int(fraction[0])
            y = int(fraction[1])
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x > y:
                pass
            elif y == 0:
                pass
            else:
                return int(round(x/y * 100))


main()
