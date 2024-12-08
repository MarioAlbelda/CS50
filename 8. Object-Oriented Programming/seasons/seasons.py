from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    print(f"{minutes(input('Date of Birth: '))} minutes")


def minutes(m):
    try:
        today = date.today()
        year, month, day = map(int, m.split("-"))
        birth = date(year, month, day)
        minutes_diff = int((today - birth).total_seconds() / 60)
        words = p.number_to_words(minutes_diff, andword="")
        return words.capitalize()
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
