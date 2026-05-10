girls = ["Liz", "Mary", "Rey"]
boys = ["Jack", "Jim", "John"]

list1 = [girls, boys]
print(list1)
# [["Liz", "Mary", "Rey"], ["Jack", "Jim", "John"]]

for dd in list1:
    for person in dd:
        print(dd, person)
# ['Liz', 'Mary', 'Rey'] Liz
# ['Liz', 'Mary', 'Rey'] Mary
# ['Liz', 'Mary', 'Rey'] Rey
# ['Jack', 'Jim', 'John'] Jack
# ['Jack', 'Jim', 'John'] Jim
# ['Jack', 'Jim', 'John'] John


for girl, boy in zip(girls, boys):
    print(girl, boy)
# Liz Jack
# Mary Jim
# Rey John
