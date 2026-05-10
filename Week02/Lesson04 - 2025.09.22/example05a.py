"""
Shopping List

"""

message = "Welcome to shopping list program \nfor exit program press q"

print(message)
vegetables = []
while True:
    vegetable = input("What do you want to buy: ")
    if vegetable.lower() == "q":
        print("shopping list: ", vegetables)
        break
    elif vegetable == "":
        continue
    else:
        vegetables.append(vegetable)
