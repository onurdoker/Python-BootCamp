"""
Break, Continue and Pass Statements
"""

# Pass Statement
if True:
    pass

print("Hello")

# Break Statement
for dd in range(10):
    name = input("Please enter your name: ")
    if name.lower() == "onur":
        print("Student found")
        break
    print(f"asked {dd + 1}. student")

# Continue Statement
for dd in range(10):
    name = input("Please enter your name: ")
    if name.lower() == "onur":
        print("Already registered student")
        continue
    surname = input("Please enter your surname")
    print(f"Welcome {name} {surname}")
