import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if not re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        return False

    parts = ip.split(".")
    for part in parts:
        try:
            num = int(part)
        except ValueError:
            return False
        if num < 0 or num > 255:
            return False
    return True

if __name__ == "__main__":
    main()