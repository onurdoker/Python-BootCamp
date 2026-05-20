# * Usage with functions that take parameters

"""
If the function to be decorated takes parameters, the wrapper function must also take those parameters

def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before function calling")
        function(*args, **kwargs)
        print("After function calling")
    return wrapper

@decorator
def function(*args, **kwargs):
   print("Function calling")

function(*args, **kwargs)
"""


def changecase(n):
    def changecase(function):
        def myinner():
            if n == 1:
                a = function().lower()
            else:
                a = function().upper()
            return a

        return myinner

    return changecase


@changecase(2)
def myfunction():
    return "Function calling"


print(myfunction())
