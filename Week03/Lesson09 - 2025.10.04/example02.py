"""
! Enclosing Scope

x parameter define in function. It is accessible inside the function and sub-functions,
but you can't change value of x in subfunction

"""


def function():
    x = 300

    def inner_function():
        print(x)
        # x = 4000
        # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

    inner_function()


function()
