def main():
    s = input("Input: ")
    print(shorten(s))


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    main()