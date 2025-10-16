from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birth_str = input("Date of Birth (YYYY-MM-DD): ")
    try:
        year, month, day = map(int, birth_str.split("-"))
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    minutes = calculate_minutes(birth_date, today)
    words = number_to_words(minutes)
    print(f"{words} minutes")

def calculate_minutes(birth_date, today):
    delta = today - birth_date  
    return round(delta.days * 24 * 60)

def number_to_words(n):
    return p.number_to_words(n, andword="").capitalize()

if __name__ == "__main__":
    main()