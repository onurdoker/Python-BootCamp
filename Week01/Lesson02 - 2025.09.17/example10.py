"""
The shorthand for the if function
"""

a = 2
if a <= 4:
    answer = "less"
else:
    answer = "greater"
print(answer)

# Shorthand version of above code
answer = "less" if a <= 4 else "greater"
print(answer)

# Shorthand version of above code
print("less" if a <= 4 else "greater")

# Another version of above code
print("less") if a <= 4 else print("greater")
