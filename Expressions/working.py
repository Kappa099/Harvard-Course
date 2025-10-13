import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(
        r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",
        s
    )
    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1 = int(h1)
    h2 = int(h2)

    if not (1 <= h1 <= 12 and 0 <= m1 < 60):
        raise ValueError("Invalid start time")
    if not (1 <= h2 <= 12 and 0 <= m2 < 60):
        raise ValueError("Invalid end time")

    h1 = to_24(h1, p1)
    h2 = to_24(h2, p2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

def to_24(hour, period):
    if period == "AM":
        if hour == 12:
            return 0
        return hour
    else: 
        if hour != 12:
            return hour + 12
        return hour

if __name__ == "__main__":
    main()