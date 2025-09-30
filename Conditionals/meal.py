def main():
    time = input("What time is it? ")
    converted = convert(time)

    if converted is None:
            return
    
    if 7 <= converted <= 8:
        print("Breakfast time")
    elif 12 <= converted <= 13:
        print("Lunch time")
    elif 18 <= converted <= 19:
        print("Dinner time")
    else:
        pass


def convert(time):
    if ":" in time:    
        hours, minutes = time.split(":")
        return int(hours) + int(minutes) / 60
    else:
        print("Incorrect format enter Hour:Minute ")
        return None



if __name__ == "__main__":
    main()