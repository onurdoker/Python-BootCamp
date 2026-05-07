name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

for dd in range(age):
    print("{} times {}".format(dd + 1, name))
