"""
! Global Scope

Global keyword is used to modify global variable inside function
"""

x = 300


def function():
    global x
    x = 400
    print("inside function, after global keyword, x: ", x)  # 400


print("before function, x: ", x)  # 300
function()
print("after function, x: ", x)  # 400
