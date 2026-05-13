"""
Demonstrates exception handling with a fruit list, catching ValueError and IndexError.
"""

print("===== FRUIT LIST =====")
fruits = ["Apple", "Pear", "Strawberry", "Banana", "Orange"]
print(f"Fruits: {fruits}")

try:
    index = int(input("Enter which fruit you want (0-4): "))

    selected_fruit = fruits[index]

    print(f"Selected fruit: {selected_fruit}")

except ValueError:
    print("Error: Value entered is not an integer (For example: 1)")

except IndexError:
    print("Error: Index out of range (0-4)")

else:
    print("Bon appetit")

finally:
    print("Program finished successfully")
