"""
the owen is heating up, with temperatures increasing in 50, 100 and 150ºC steps. But a warning 'Caution: Medium temperature' is given it reaches 100ºC, but the process continues. We should write code to say 'Ready!' when it reaches 200ºC.
"""

# * First method
temp = 0
while temp <= 200:
    temp += 50
    if temp == 100:
        print("Owen temperature reach 100ºC")
        print("Caution: Medium temperature")
        continue
    elif temp == 200:
        print("Owen temperature reached 200ºC")
        print("Ready!")
        break
    print(f"Owen temperature is {temp}")

# * Second method (Using match case)
temp = 0
while temp <= 200:
    temp += 50
    match temp:
        case 100:
            print("Owen temperature reached 100ºC")
            print("Caution: Medium temperature")
            continue
        case 200:
            print("Owen temperature reached 200ºC")
            print("Ready!")
            break
        case _:
            print(f"Owen temperature is {temp}")
