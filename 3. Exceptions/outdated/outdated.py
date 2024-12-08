months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        date = str(input("Date: "))
        num = date.split("/")
        month = int(num[0])
        day = int(num[1])
        year = int(num[2])

    except ValueError:
        try:
            date = date.split(",")
            year = int(date[1])
            first = date[0].split(" ")
            month = str(first[0])
            day = int(first[1])

        except IndexError:
            continue

        except ValueError:
            continue

        else:
            if month in months_list:
                month = months_list.index(month)+1
                if month < 0 or month > 12 or day > 31:
                    continue
                else:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            else:
                pass

    except EOFError:
        print("")
        break

    else:
        if month < 0 or month > 12 or day > 31:
            continue
        else:
            print(f"{year}-{month:02}-{day:02}")
            break
