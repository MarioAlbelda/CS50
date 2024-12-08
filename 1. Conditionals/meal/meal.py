def main():
    hour = convert(input("What time is it? "))
    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(int(hours) + (int(minutes) / 60))


if __name__ == "__main__":
    main()
