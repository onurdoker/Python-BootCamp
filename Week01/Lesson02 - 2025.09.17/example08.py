"""
Nested Conditional Statements
Structures we use to perform conditional operations and logic with multiple conditions.
"""

score = int(input("Please enter you average GPE score: "))

if score < 0:
    print("Invalid average GPE score. Please try again.")
else:
    if score < 70:
        print("You can't obtain a certification.")
    else:
        if score < 85:
            print("You can obtain a certification of gratitude.")
        else:
            if score <= 100:
                print('"You can obtain a certification of appreciation."')
            else:
                print("Invalid average GPE score. Please try again.")
