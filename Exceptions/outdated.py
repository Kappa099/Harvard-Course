months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.strip().split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        elif "," in date:

            parts = date.replace(",", ", ").split()
            if len(parts) != 3:
                continue 
            month_name = parts[0].capitalize()
            day = int(parts[1].replace(",", ""))
            year = int(parts[2])
            if month_name not in months:
                continue
            month = months.index(month_name) + 1

        else:
            continue 

        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue  

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except (ValueError, IndexError):
        continue
