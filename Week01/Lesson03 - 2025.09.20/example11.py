"""
Multiplication Table
"""

for x in range(1, 11):
    print("#{}".format(x))
    for y in range(1, 11):
        print("\t {}*{} = {}".format(x, y, x * y))
