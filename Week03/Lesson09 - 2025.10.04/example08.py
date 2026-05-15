"""
Readline => Read line by line
"""

# First method
with open("file.txt", "r") as file:
    for x in file:
        print(x)

# Second method
with open("file.txt", "r") as file:
    for x in file:
        print(x)


# Third method
with open("file.txt", "r") as file:
    text = file.read()
    print("text: \n", text)
    lines = text.split("\n")
    print("\nlines: \n", lines)
