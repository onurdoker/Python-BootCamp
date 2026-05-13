"""
This program validates a password by checking its length, character types, and returns an error message if any condition is not met.
"""


def control_password(password):
    if len(password) < 8:
        return "Password has at least 8 characters."
    elif len(password) > 16:
        return "Password has at most 16 characters."
    elif password.isnumeric():
        return "Password contains only numeric characters."
    elif password.isalnum():
        return "Password has at least one special character."
    elif password.isalpha():
        return "Password has at one number."
    elif password.lower() == password:
        return "Password has at least one uppercase letter"
    elif password.upper() == password:
        return "Password has at least one lowercase letter"
    else:
        return "Password is valid"


password = input("Please enter your new password: ")

print(control_password(password))
