"""
To calculate the total amount spent and received during a market shopping trip
"""

items = {}

print("Please enter your items and prices")
print("to exit enter quit")

while True:
    name = input("Enter your item: ")
    if name.lower() == "quit":
        break
    price = float(input("Please enter item's price: "))
    items[name] = price

print(items)
total_price = sum(items.values())
print(f"Total price is {total_price}")
