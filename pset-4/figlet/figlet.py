import sys
from pyfiglet import Figlet
import random

cli_args = ["-f", "--font"]
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3 and sys.argv[1] in cli_args and sys.argv[2] in fonts:
	f = sys.argv[2]	
elif len(sys.argv) == 1:
	f = random.choice(fonts)
else:
	sys.exit("Invalid command line arguments")

figlet.setFont(font=f)
user_input = input("Input: ")
print("Output:")
print(figlet.renderText(user_input))
