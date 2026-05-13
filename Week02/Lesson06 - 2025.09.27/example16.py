"""
**kwargs
"""


def student_knowledge(**kwargs):
    print(
        kwargs, type(kwargs)
    )  # {'name': 'John', 'surname': 'Doe', 'no': 153, 'attendance': True, 'average': 3.6} <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key} : {value}")


student_knowledge(name="John", surname="Doe", no=153, attendance=True, average=3.6)
