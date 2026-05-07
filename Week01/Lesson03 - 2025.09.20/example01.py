"""
Loops

For loops -> The for loop is used when the order of operations is known and the operation needs to be performed multiple times.

While loops -> The while loop is used when a logical query needs to be executed and the operation continues until it is logically completed.
"""

print(range(10))  # range(0, 10)
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for loop
# range function -> range(stop) (default start = 0, step = 1)
for dd in range(5):  # dd-> 0, 1, 2, 3, 4,
    print(dd + 1, ". slice of pizza")
# 1 . slice of pizza
# 2 . slice of pizza
# 3 . slice of pizza
# 4 . slice of pizza
# 5 . slice of pizza

# range function -> range(start, stop) (default step = 1)
for dd in range(1, 6):  # dd-> 1, 2, 3, 4, 5
    print(dd, ". slice of pizza")
# 1 . slice of pizza
# 2 . slice of pizza
# 3 . slice of pizza
# 4 . slice of pizza
# 5 . slice of pizza

# range function -> range(start, stop, step)
for dd in range(2, 10, 2):  # dd-> 2, 4, 6, 8,
    print(dd, ". slice of pizza")
# 2 . slice of pizza
# 4 . slice of pizza
# 6 . slice of pizza
# 8 . slice of pizza
