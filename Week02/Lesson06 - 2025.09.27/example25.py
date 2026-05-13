"""Generates Fibonacci series up to a specified number of terms."""


def fibonacci_series(number):
    series = []
    number1, number2 = 0, 1
    for pp in range(number):
        series.append(number1)
        number1, number2 = number2, number2 + number1
    return series


print(fibonacci_series(10))
