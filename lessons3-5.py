"""
Name: Delaina Poppleton
Date: 12-4-24
Topics: Immutability, for loops, in keyword
"""

# Immutability - a string cannot be mutated or changed using [ ];
# you must replace it completely

cat_name = "Franklin"
cat_name = cat_name[0:5]+"ie"
print(cat_name)

# For loops and strings

# You can go character by character through a string. This is called
# traversing a string

# Non-Pythonic way
cat_name = "Winston"
for i in range(len(cat_name)):
    print(cat_name[i])

for i in range(len(cat_name)): #print Win
    print(cat_name[i])
    if cat_name[i] == "n":
        break

# The in keyword
vowels = "aeiou"
print("a" in vowels)
print("b" in vowels)

# Use #1 - Determine if a substring is in a string
for i in range(len(cat_name)): #print Win
    if cat_name[i] in vowels:
        print(cat_name[i])

print("Win" in cat_name)


# Use #2 - Pythonic traversal
cat_name = "Millie"
for letter in cat_name:
    print(letter, end = " ")
print()
large_number = 2308408290849032
for digit in str(large_number):
    print(digit,end = " ")

print("\n-------")
print(str(123) in str(12345))


