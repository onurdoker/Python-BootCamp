import json

user = {
    "name": "Jack",
    "age": 25,
    "city": "New York",
    "hobbies": ["sport", "music", "traveling"],
    "active": True,
}

# Converting to JSON string
json_string = json.dumps(user, ensure_ascii=False, indent=2)
print("JSON string: ")
print(json_string)

# Creating JSON file
with open("user.json", "w", encoding="UTF-8") as file:
    json.dump(user, file, ensure_ascii=False, indent=4)


# Reading JSON file and printing the data
with open("user.json", "r", encoding="UTF-8") as file:
    data = json.load(file)
    print("\n Data loaded from JSON file:")
    print(data)
