# Write a program in Python that displays how many vowels are in a string.

string = (input("Enter a string: "))

vowels = 0

for i in string:
    if (
            i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
        vowels = vowels + 1

print("Number of vowels is", vowels, ".")
