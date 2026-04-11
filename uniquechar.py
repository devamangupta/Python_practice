text = input("Enter a text:")
unique_text =""
for i in text:
    if i not in unique_text:
        unique_text += i
print("Result", unique_text)