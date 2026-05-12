products = [
    {"name": "laptop", "price": 25000, "stock": 30},
    {"name": "mouse", "price": 25, "stock": 450},
    {"name": "keyboard", "price": 41, "stock": 39},
]

for product in products:
    print(product)
    print(f"{product['name']} - {product['price']} - {product['stock']} ")
# {"name": "laptop", "price": 25000, "stock": 30}
# laptop - 25000 - 30
# {"name": "mouse", "price": 25, "stock": 450}
# mouse - 25 - 450
# {"name": "keyboard", "price": 41, "stock": 39}
# keyboard - 41 - 39
