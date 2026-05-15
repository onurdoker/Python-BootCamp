"""
Reading data from file
"""

with open("file.txt", "r") as file:
    content = file.read()
    print(len(content), type(content))

    content2 = file.read()
    print(len(content2), type(content2))
    print(content2)
