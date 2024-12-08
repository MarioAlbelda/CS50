import sys
import csv

students = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1], "r") as before:
            reader = csv.DictReader(before)
            for row in reader:
                last, first = row["name"].rstrip().split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})
        with open(sys.argv[2], "w") as after:
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit("File does not exist")
