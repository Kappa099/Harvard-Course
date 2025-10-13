import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: python lines.py <filename>")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Error: File must end with .py")

if not os.path.isfile(filename):
    sys.exit(f"Error: File '{filename}' does not exist")

loc = 0
with open(filename, 'r') as file:
    for line in file:
        stripped = line.lstrip()
        if stripped.strip() == "" or stripped.startswith("#"):
            continue
        loc += 1

print(loc)