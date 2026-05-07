"""
Write a code that concatenates all the words entered by the user until the user type 'exit'
"""

sentence = ""

while True:
    word = input("Please a word: ")
    if word.lower() == "exit":
        break
    else:
        sentence += word

print(f"Your sentence is {sentence}")
