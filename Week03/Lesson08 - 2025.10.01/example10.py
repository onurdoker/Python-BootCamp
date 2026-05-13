"""
Demonstrates serialization and deserialization using Python's 'json' module.
"""

import json

# * Converting python object to json string

data = {"name": "John", "age": 30, "cities": ["New York", "Los Angles", "Chicago"]}
print(data)
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print("JSON string:\n", json_str, "\n", type(json_str))

# * Converting json string to python object
parsed = json.loads(json_str)
print(type(parsed))  # <class 'dict'>
print(parsed["name"])  # John
