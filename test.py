# # most_frequent("hello world") ➞ ('l', 3)
# # most_frequent("aabbbccde") ➞ ('b', 3)

# text = input("Enter a text: ")
# dictru = {}
# for char in text:
#     if char in dictru:
#         dictru[char] += 1
#     else:
#         dictru[char] = 1
# most_frequent = max(dictru, key=dictru.get)
# print(f"Most frequent character: '{most_frequent}' ({dictru[most_frequent]} times)")


# def filter_long_words(text, n):
#     words = text.split()
#     longs = []
#     for word in words:
#         if len(word) > n:
#             longs.append(word)
#     return longs

# print(filter_long_words("The quick brown fox jumps over the lazy dog", 4))


# def remove_duplicates(lst):
#     result = []
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result

# text1 = [1, 2, 2, 3, 1, 4, 2]
# text2 = ["a", "b", "a", "c", "b"]

# print(remove_duplicates(text1)) 
# print(remove_duplicates(text2))  

# second_largest([10, 20, 4, 45, 99])     # ➞ 45
# second_largest([1, 1, 1, 1])            # ➞ None or custom message
# second_largest([5])                     # ➞ None or custom message

# def number_checked(lst):

#     for num in lst:
#         if len(lst) > 1:
#             if len(set(lst)) > 0:
#                 pass
#             else:
#                 print(None)
#         else:
#             print(None)

# name = input("Enter your Name: ")
# print(f'Hello {name}')

# name = "Vako"
# age = 26
# city = "Tbilisi"

# print(f'My name is {name}, I am {age} years old and I live in {city}')

# UserString = input("Enter a string")

# Upper = UserString.upper()
# lower = UserString.lower()
# title = UserString.title()
# reversed = UserString[::-1]
# print(Upper)
# print(lower)
# print(title)
# print(reversed)

# text = input("Enter text: ")
# print(f"Letter 'A' in text was {text.upper().count('A')} times")

# def say_hello():
#     print("Hello")

# say_hello()

# def greet(name):
#     print(f"Hello {name}")

# user = input("Enter your name: ")
# greet(user)

# def add(a, b):
#     return(a + b)

# result = add(5, 10)
# print(result)

# def is_even(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# result = is_even(int(input("Enter a Number: ")))
# print(result)

# def compare(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     elif num3 > num2 and num3 > num1:
#         return num3
#     else:
#         print("Equal numbers")

# numbers = compare(5,20,15)
# print(numbers)


# def compare(*args):
#     if not args:
#         return "No numbers provided"
#     biggest = args[0]
#     for num in args[1:]:
#         if num > biggest:
#             biggest = num
#     return biggest

# numbers = compare(5,20,15,50,55,22)
# print(numbers)

# def palindrome(text):
#     word = text.lower().strip()
#     if word == word[::-1]:
#         return f"{word} is Palindrome"
#     else:
#         return f"{word} is not Palindrome"

# text = palindrome("Racecar")
# print(text)
# 
# 
#