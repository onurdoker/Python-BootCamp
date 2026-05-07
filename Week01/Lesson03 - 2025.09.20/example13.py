"""
Password checker
"""

try_ = 3
correct_password = "python123"

while try_ > 0:
    password = input("Please enter your password ")

    if password == correct_password:
        print("Entered correct password")
        break
    else:
        try_ -= 1
        print("Incorrect password, please try again.")
        print(f"You have {try_} tries left.")

# if try_ == 0:
#     print("You have exceeded the maximum number of attempts. Access denied.")

else:
    print("You have exceeded the maximum number of attempts. Access denied.")
