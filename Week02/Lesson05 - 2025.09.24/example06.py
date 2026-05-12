"""
Turkish - English Dictionary example
"""

tr_eng = {"araba": "car", "kalem": "pencil", "kırmızı": "red"}
print(tr_eng)  # {'araba': 'car', 'kalem': 'pencil', 'kırmızı': 'red'}

for key, value in zip(tr_eng.keys(), tr_eng.values()):
    print(key, "=>", value)
# araba => car
# kalem => pencil
# kırmızı => red

# Adding a new word to the dictionary
tr_eng["mavi"] = "blue"
print(tr_eng)
