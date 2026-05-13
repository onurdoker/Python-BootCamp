"""
This file demonstrates two methods to swap dictionary keys and values: using a for loop and dictionary comprehension.
"""


def key_value_changer(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict


tr_en_dict = {"kırmızı": "red", "mavi": "blue", "yeşil": "green"}
en_tr_dict = key_value_changer(tr_en_dict)
print(f"Reverse of tr_en_dict: {en_tr_dict}")


def key_value_changer2(dict):
    return {value: key for key, value in dict.items()}


tr_en_dict = {"kırmızı": "red", "mavi": "blue", "yeşil": "green"}
en_tr_dict = key_value_changer2(tr_en_dict)
print(f"Reverse of tr_en_dict: {en_tr_dict}")
