# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

answer = str(input("Hello Please enter a file name. Example: cat.gif ")).strip().lower()

if answer.endswith(".gif"):
    print("image/gif")
elif answer.endswith(".jpg"):
    print("image/jpg")
elif answer.endswith(".jpeg"):
    print("image/jpeg")
elif answer.endswith(".png"):
    print("image/png")
elif answer.endswith(".pdf"):
    print("application/pdf")
elif answer.endswith(".txt"):
    print("text/plain")
elif answer.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
