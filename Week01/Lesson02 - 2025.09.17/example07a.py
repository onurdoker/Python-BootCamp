meal = input("Enter food name: ")
drink = input("Enter drink name: ")

# Let's elaborate on our questions furher
if meal == "pizza" and (drink == "cola" or drink == "ayran"):
    print("Valid order")
    print("Bon apetite! Enjoy your meal!")
else:
    print(f"{meal} - {drink} is not valid order")
