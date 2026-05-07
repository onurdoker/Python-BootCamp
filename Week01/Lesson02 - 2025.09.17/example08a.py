score = int(input("Please enter you average GPE score: "))

if score < 0:
    print("Invalid average GPE score. Please try again.")
elif score < 70:
    print("You can't obtain a certification.")
elif score < 85:
    print("You can obtain a certification of gratitude.")
elif score <= 100:
    print('"You can obtain a certification of appreciation."')
else:
    print("Invalid average GPE score. Please try again.")
