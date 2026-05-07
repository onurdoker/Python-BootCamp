"""
Write a code to reverse a given sentence
"""

# * First method
sentence = input("Please enter your sentence: ")
reverse_sentence = ""

for letter in range(len(sentence) - 1, -1, -1):
    reverse_sentence += sentence[letter]

print(f"Reverse version of the '{sentence}' is '{reverse_sentence}' ")

# * Second method
sentence = input("Please enter your sentence: ")
reverse_sentence = ""

for letter in sentence:
    reverse_sentence = letter + reverse_sentence

print(f"Reverse version of the '{sentence}' is '{reverse_sentence}'")
