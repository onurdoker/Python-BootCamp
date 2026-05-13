"""
**kwargs
"""


def item_entry(**kwargs):
    item = {}
    for key, value in kwargs.items():
        item[key] = value
    return item


laptop = item_entry(name="iPad Mac", item_price=15000, stock=30)
print(laptop, type(laptop))
# {'name': 'iPad Mac', 'item_price': 15000, 'stock': 30} <class 'dict'>
