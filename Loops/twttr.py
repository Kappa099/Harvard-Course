vowels = ["a","e","i","o","u"]
text = input("Input: ")
result = ""
for character in text:
    if character not in vowels:
        print(character,end="")
