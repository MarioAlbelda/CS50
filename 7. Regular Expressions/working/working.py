import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(?P<hours1>\d{1,2})(:(?P<minutes1>\d{2}))? (?P<MD1>(AM|PM)) to (?P<hours2>\d{1,2})(:(?P<minutes2>\d{2}))? (?P<MD2>(AM|PM))$", s):
        hours1 = int(matches.group("hours1"))
        hours2 = int(matches.group("hours2"))

        minutes1 = int(matches.group("minutes1")) if matches.group("minutes1") else 0
        minutes2 = int(matches.group("minutes2")) if matches.group("minutes2") else 0

        if hours1 > 12 or hours2 > 12 or minutes1 > 59 or minutes2 > 59:
            raise ValueError

        if matches.group("MD1") == "PM" and hours1 != 12:
            hours1 += 12
        if matches.group("MD2") == "PM" and hours2 != 12:
            hours2 += 12
        if matches.group("MD1") == "AM" and hours1 == 12:
            hours1 = 0
        if matches.group("MD2") == "AM" and hours2 == 12:
            hours2 = 0

        return(f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}")

    else:
        raise ValueError

if __name__ == "__main__":
    main()
