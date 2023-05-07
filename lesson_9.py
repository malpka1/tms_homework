# 1.Создать родительский класс машина, у которого есть атрибуты model,age, color и weight,
# из них обязательный только model. Также у класса должны
# быть методы move, stop, birthday, методы move и stop выводят сообщение на
# экран "move", "stop", а birthday увеличивает атрибут age на 1. Если атрибут age =
# None, то выбрасывает исключение с сообщением "атрибут age не задан".
import age as age
import self as self

class Cars:
    def __init__(self, model, age=None, color=None, weight=None):
        self.model = model
        self.age = age
        self.color = color
        self.weight = weight
    def move(self):
        print("move")
    def stop(self):
        print("stop")
    def birthday(self):
        if self.age is None:
            raise ValueError("Attribute age is not set")
        else:
            self.age += 1
car = Cars("Hyundai")
car.age = 10
print(car.age)
print(car.move())

#2.Есть csv файл со списком людей, нужно прочитать его и преобразовать в список датаклассов.
# То есть нужно создать датакласс с атрибутами name, age,
# при этом тип age : Optional[int]. У датакласса должно быть property birth_year, которое считает возраст
import csv
from typing import Optional

class Person:
    def __init__(self, name: str, age: Optional[int]):
        self.name = name
        self.age = age

    @property
    def birth_year(self):
        if self.age is None:
            return None
        else:
            return 2023 - self.age

def read_csv(file_path):
    people = []
    with open(file_path) as f:
        reader = csv.reader(f)
        next(reader) # skip header row
        for row in reader:
            name = row[0]
            age = int(row[1]) if row[1] else None
            person = Person(name, age)
            people.append(person)
    return people

people = [
    Person("Лена", 24),
    Person("Дима", None),
    Person("Вова", 35)
]

for person in people:
    print(person.name, person.age, person.birth_year)