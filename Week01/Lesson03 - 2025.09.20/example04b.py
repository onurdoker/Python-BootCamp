piece = int(input("How many pieces of pizza do you want? "))

for slice in range(1, piece + 1):
    print(slice, ". piece of pizza.")
    print("Slices left: {}".format(piece - slice))
