import sys
import os
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

if not os.path.isfile(filename):
    sys.exit("File does not exist")

rows = []
with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)

print(tabulate(rows, headers="keys", tablefmt="grid"))