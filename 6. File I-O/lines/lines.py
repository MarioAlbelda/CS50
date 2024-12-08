import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        i = 0
        with open(sys.argv[1], "r") as file:
            for line in file:
                line_content = line.lstrip()
                if line_content == "":
                    continue
                elif line_content.startswith("#"):
                    continue
                else:
                    i += 1
        print(i)
    except FileNotFoundError:
        sys.exit("File does not exist")
