"""
! Global Scope

"""

x = 300


def function():
    y = 500
    print("inside function, x: ", x)  # 300
    print("inside function, y: ", y)  # 500
    # print("inside function, z: ", z)  # NameError: name 'z' is not defined

    def inner_function():
        z = 600
        print("inside inner_function, x: ", x)
        print("inside inner_function, y: ", y)
        print("inside inner_function, z: ", z)

    print(
        "inside function, outside inner function, before inner_function, x: ", x
    )  # 300
    print(
        "inside function, outside inner function, before inner_function, y: ", y
    )  # 500
    # print("inside function, outside inner function, before inner_function, z: ", z)  # NameError: name 'z' is not defined

    inner_function()
    print(
        "inside function, outside inner function, after inner_function, x: ", x
    )  # 300
    print(
        "inside function, outside inner function, after inner_function, y: ", y
    )  # 500
    # print("inside function, outside inner function, after inner_function, z: ", z)  # NameError: name 'z' is not defined


print("outside function, before function, x: ", x)  # 300
# print("outside function, before function, y: ", y)  # NameError: name 'y' is not defined
# print("outside function, before function, z: ", z)  # NameError: name 'z' is not defined
function()
print("outside function, after function, x: ", x)  # 300
# print("outside function, after function, y: ", y)  # NameError: name 'y' is not defined
# print("outside function, after function, z: ", z)  # NameError: name 'z' is not defined
