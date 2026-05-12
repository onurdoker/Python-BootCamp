"""
Take product name, price and stock quantities form the user and add them to a dictionary list
"""

print("=" * 5, "Product Stock System", "=" * 5)
print("to exit write quit")

products = []
while True:
    name = input("Please enter product's name: ")
    if name.lower() == "quit":
        break
    else:
        price = float(input("Please enter product's price: "))
        if price < 0.0:
            break

        stock = int(input("Please enter product's stock quantity: "))
        if stock < 0:
            break

        products.append({"name": name, "price": price, "stock": stock})

print(products)
