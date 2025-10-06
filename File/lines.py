import sys

if len(sys.argv) != 2:
    print("Usage: python file.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"File '{filename}' not found.")
