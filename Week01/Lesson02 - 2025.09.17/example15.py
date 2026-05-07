"""
print
"""

# default separator is space
print("omer", "gamze", "yasin")  # omer gamze yasin

print("omer", "gamze", "yasin", sep=", ")  # omer, gamze, yasin

# separator attribute can be assigned to a variable
print("omer", "gamze", "yasin", sep="*")  # omer*gamze*yasin
print("omer", "gamze", "yasin", sep="-----")  # omer-----gamze-----yasin
print("omer", "gamze", "yasin", sep="\t")  # omer	gamze	yasin

# end attribute can be assigned to a variable
print("omer", "gamze", "yasin", end="+++")  # omer gamze yasin+++
