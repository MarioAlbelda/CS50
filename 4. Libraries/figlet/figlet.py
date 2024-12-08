import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

# No command-line argument
if len(sys.argv) == 1:
    figlet.setFont(font=choice(figlet.getFonts()))
    text = str(input("Input: "))
    figlet.setFont(font= random.choice(fonts))
    print("Output:")
    print(figlet.renderText(text))

# Two command-line arguments
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
    print("Output:", figlet.renderText(input("Input: ")), sep="\n")

else:
    sys.exit("Invalid usage")
