#1 Дописать функцию так, чтобы она возвращала None в случае если ключа нет, а не генерировала исключение (для реализации используем исключения)
def func(dict_, key):
    try:
        return dict_[key]
    except KeyError:
        return None
my_dict = {'name':'Igor', 'age':30}
print(func(my_dict, 'name'))
print(func(my_dict, 'surname'))

#2
string1 = "I'm Slim Shady, yes I'm the real Shady"
string2 = "All you other Slim Shadys are just imitating"
string3 = "So won't the real Slim Shady please stand up"
string4 = "please stand up, please stand up"

with open('task2.txt', 'a') as f:
    f.write(string3 + '\n')
    f.write(string4 + '\n')
#3
import json
my_dict = [
    {"id": 123456, "name":"Andrei", "age": 20},
    {"id": 234567, "name":"Boris", "age": 30},
    {"id": 345678, "name":"Peter", "age": 40},
    {"id": 456789, "name":"Sveta", "age": 50},
    {"id": 567890, "name":"Roma", "age": 60},
    {"id": 678900, "name":"Oleg", "age": 70},
]
with open("my_dict.json", "w") as f:
    json.dump(my_dict, f)
with open("my_dict.json", "r") as f:
        my_dict = json.load(f)
print(my_dict)

import csv
with open("my_dict.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(my_dict[0].keys())
    for row in my_dict:
        writer.writerow(row.values())








