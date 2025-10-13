import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py before.csv after.csv")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "r", newline="") as infile:
        reader = csv.DictReader(infile)
        
        cleaned_rows = []
        for row in reader:
            last, first = row["name"].split(", ")
            cleaned_rows.append({
                "first": first,
                "last": last,
                "house": row["house"]
            })
except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

with open(output_file, "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(cleaned_rows)