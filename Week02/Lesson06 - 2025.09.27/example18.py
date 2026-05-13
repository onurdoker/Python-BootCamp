"""
Using *args and **kwargs together in a function definition.
"""


def student_cart(*args, **kwargs):
    print(args, type(args))  # ('Student Information Cart',) <class 'tuple'>
    print(
        kwargs, type(kwargs)
    )  # {'student_name': 'John', 'student_surname': 'Dow', 'student_department': 'Chemical Engineering'} <class 'dict'>
    for cart_knowledge in args:
        print(cart_knowledge)
        for knowledge in kwargs:
            print(knowledge, ":", kwargs[knowledge])


student_cart(
    "Student Information Cart",
    student_name="John",
    student_surname="Dow",
    student_department="Chemical Engineering",
)

# Student Information Cart
# student_name : John
# student_surname : Dow
# student_department : Chemical Engineering
