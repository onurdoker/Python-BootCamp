meal = input("Enter food name: ")
drink = input("Enter drink name: ")

# Let's elaborate on our questions furher
if meal == "pizza":
    print("Pizza is a valid meal order.")
    if drink == "cola" or drink == "ayran":
        print("Valid order")
        print("Bon apetite! Enjoy your meal!")
    else:
        print(f"{drink} can be returned")
else:
    print(f"{meal} is not valid order")
