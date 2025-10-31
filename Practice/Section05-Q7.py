"""
Ask the user for n numbers and then display which number was entered how many times.
"""

from collections import Counter


def count_numbers():
    n = int(input("Please enter the number of integer you want to input: "))

    numbers = []

    for i in range(n):
        number = int(input(f"Please enter your {i+1} number: "))
        numbers.append(number)

    counts = Counter(numbers)

    print("\nResults:")
    for number, freq in counts.items():
        print(f"The number {number} is {freq} times.")


count_numbers()
