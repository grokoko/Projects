# Zliczanie samogłosek

message = input("Enter a message: ")
counter = 0
vowels = ["a", "e", "i", "o", "u", "y"]

for letter in message:
    for vow in vowels:
        if letter.lower == vow:
            counter += 1

print("There are", counter, "vowels in your message.")

input("\n\nEnter")