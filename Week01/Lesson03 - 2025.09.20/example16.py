"""
Count the number of 'a' letters in a sentences entered by the user
"""

# * First method
sentence = input("Please enter your sentences: ")
count = 0

words = sentence.split()
for word in words:
    for letter in word:
        if letter.lower() == "a":
            count += 1
print(f'Number of "a" in the {sentence} is {count} ')

# * Second method
sentence = input("Please enter your sentence: ")
count = 0

for letter in sentence:
    if letter.lower() == "a":
        count += 1

print(f'Number of "a" in the {sentence} is {count} ')
