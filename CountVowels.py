# Zliczanie samogłosek

message = input("Enter a message: ")
counter = 0
a = 0
e = 0
i = 0
o = 0
u = 0
vowels = ["a", "e", "i", "o", "u"]

for letter in message:
    for vow in vowels:
        if letter.lower() == vow:
            counter += 1
            if letter.lower() == "a":
                a += 1
            elif letter.lower() == "e":
                e += 1
            elif letter.lower() == "i":
                i += 1
            elif letter.lower() == "o":
                o += 1
            elif letter.lower() == "u":
                u += 1

print("There are", counter, "vowels in your message.")
print("Exactly there are", a, "a,", e, "e,", i, "i,", o, "o and", u, "u.")

input("\n\nEnter")