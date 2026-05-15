class Book:
    name = ""
    author = ""
    page_number = 0
    publisher = ""
    print_year = ""


book1 = Book()
book1.name = "Animal Farm"
book1.author = "George Orweel"
book1.page_number = 80
book1.publisher = "TechIstanbul"
book1.print_year = 1950

print(book1.name)  # Animal Farm

variables = vars(book1)
print(variables, type(variables))
# {'name': 'Animal Farm', 'author': 'George Orweel', 'page_number': 80, 'publisher': 'TechIstanbul', 'print_year': 1950}  <class 'dict'>
