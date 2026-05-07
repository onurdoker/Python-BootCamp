"""
Calculate the multiply of the first ten unique non-zero numbers entered by the user.
If the user enters a zero, it should be ignored. If the user enters more than ten unique non-zero numbers, it should stop asking for input and display the result.
"""

multiply = 1
times = 0
entered_number = ""
while True:
    number = int(input("Please enter a number to multiply: "))
    if number == 0:
        continue

    multiply *= number
    times += 1
    entered_number += str(number) + " - "

    if times == 10:
        print("You entered 10 unique numbers from zero")
        print(f"The multiplication of all numbers is {multiply}")
        print("Entered numbers: ", entered_number)
        break
