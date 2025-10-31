"""
Research the divide and conquer algorithm, without using functions calculate and print on screen the smallest and largest numbers between a range of
user-provided numbers using lists.
"""

numbers = input("Please enter numbers separated by space: ").split()

number_list = []

for number in numbers:
    number_list.append(number)


def divide_and_conquer(numbers):
    if len(numbers) == 1:
        return numbers[0], numbers[0]

    min_number = min(numbers)
    max_number = max(numbers)

    return min_number, max_number


min_number, max_number = divide_and_conquer(number_list)

print(f"The smallest number is {min_number} and largest number is {max_number}")
