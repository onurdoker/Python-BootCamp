name = "John"
letter_of_name = list(name)
print(letter_of_name)  # ['J', 'o', 'h', 'n']
print(len(letter_of_name))  # 4

new_string = str(letter_of_name)
print(new_string, type(new_string))  # ['J', 'o', 'h', 'n'] <class 'str'>
print(len(new_string))  # 20

for letter in new_string:
    print(letter)
