import sys
from tabulate import tabulate
import csv

menu = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append({reader.fieldnames[0]: row[reader.fieldnames[0]], "Small": row["Small"], "Large": row["Large"]})
        print(tabulate(menu, headers = "keys", tablefmt = "grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
