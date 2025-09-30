from emoji import emojize

text = input("Input: ").strip().lower()
if not text.startswith(":"):
    text = f":{text}"
if not text.endswith(":"):
    text = f"{text}:"
new_text = text.replace(" ", "_")
print(emojize(new_text, language='alias')) 