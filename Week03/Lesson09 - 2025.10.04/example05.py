"""
! Nonlocal Scope

Nonlocal keyword is used to modify nonlocal variable inside function
"""


def function():
    name = "John"

    def inner_function():
        nonlocal name
        name = "Jack"

        print("Inside inner_function, name: ", name)  # Jack

    print("Before inner_function call, name: ", name)  # John
    inner_function()
    print("After inner_function call", name)  # Jack
    return name


# print("before function call, name: ", name)  # NameError: name 'name' is not defined
function()
# print("After function call, name: ", name)  # NameError: name 'name' is not defined
