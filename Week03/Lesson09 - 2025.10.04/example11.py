"""
Write the code that will prompt the user to enter products, append them to a list, and print the entire file after the operation is completed.
"""

with open("Shopping_list.txt", "a") as file:
    while True:
        item = input(
            'Enter an item to add to the shopping list (or type "done" to finish): '
        )
        if item.lower() == "done":
            print("Shopping list saved successfully!")
            break
        file.write(f"{item}\n")

with open("Shopping_list.txt", "r") as file:
    print(file.read())
