"""
3. Static methods (@staticmethod)
- These methods are bound neither to the class nor to the instance.
- They behave like independent functions but are defined within a class.

- They are defined using the @staticmethod decorator and do not take self or cls as a parameter
"""


class Mathematics:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Mathematics.sum(3, 5))  # 8
print(Mathematics.multiply(3, 5))  # 15

"""
- They are ideal for helper (utility) operations
- They do not take self or cls because they cannot access instance or class data
"""
