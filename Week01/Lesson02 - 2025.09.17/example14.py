name1 = "Gamze"
name2 = "Omer"
name3 = "Yasin"

print(name1 + name2 + name3)  # GamzeOmerYasin
print(f"{name1} {name2} {name3}")  # Gamze Omer Yasin

text = "Hi Dear {}. \nWelcome to Python Bootcamp"

text.format(name1)  # Hi Dear Gamze. \nWelcome to Python Boot
print(text.format(name2))
# Hi Dear Omer
# Welcome to Python Bootcamp

print(text.format(name3))
# Hi Dear Yasin
# Welcome to Python Bootcamp


text2 = "The first, the second and the third place winners of our competition are {}, {} and {}."
print(text2.format(name1, name2, name3))
# The first, the second and the third place winners of our competition are Gamze, Omer and Yasin.


print(text2.format(name3, name2, name1))
# The first, the second and the third place winners of our competition are Yasin, Omer and Gamze.

# Counting a character in a string
print(text2.count("a"))  # 4
print(text2.count("s"))  # 3
