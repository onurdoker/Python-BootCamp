"""
This file contains a function that calculates a student's average score.
The function takes a student dictionary with scores and returns the mean.
"""


def calculate_student_score_average(student):
    total = 0
    for score in student["scores"]:
        total += score
    average_score = total / len(student["scores"])
    return average_score


student = {"name": "jon", "scores": [70, 85, 90, 65]}
average = calculate_student_score_average(student)
print(f"{student['name']} \n{average}")
