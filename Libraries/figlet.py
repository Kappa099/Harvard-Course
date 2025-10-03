import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

args = sys.argv[1:]

if len(args) == 0:
    font = random.choice(fonts)

elif len(args) == 2 and args[0] in ("-f", "--font"):
    if args[1] not in fonts:
        sys.exit("Error: Invalid font name.")
    font = args[1]

else:
    sys.exit("Usage:\n  python figlet.py\n  python figlet.py -f <font>")

figlet.setFont(font=font)

text = input("Enter text: ")
print(figlet.renderText(text))
