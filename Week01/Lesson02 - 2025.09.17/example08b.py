classroom = int(input("Please enter your class: "))

if classroom == 0:
    print("You are in the Kindergarten")
elif 1 <= classroom <= 4:
    print("You are in Primary School")
elif 5 <= classroom <= 8:
    print("You are in Secondary School")
elif 9 <= classroom <= 12:
    print("You are in High School")
else:
    print("Invalid classroom entered, please try again")
