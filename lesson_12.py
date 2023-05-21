class Animal:
    def __init__(self, name, animal_type, age=0):
        self._name = name
        self._animal_type = animal_type
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def animal_type(self):
        return self._animal_type

    @property
    def age(self):
        return self._age

    @classmethod
    def create_tiger(cls, name):
        return cls(name, 'tiger', 0)

    @classmethod
    def create_panda(cls, name):
        return cls(name, 'panda', 0)

class Zoo:
    def __init__(self, name_zoo):
        self.name = name_zoo
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def __iter__(self):
        return iter(self.animals)

    def __len__(self):
        return len(self.animals)

    def __getitem__(self, index):
        return self.animals[index]

    def __str__(self):
        return f"Zoo: {self.zoo_name}, {len(self.animals)}"

    def get_animal_by_index(self, index):
        return self.animals[index]

    def get_by_type(self,animal_type):
        return [animal for animal in self.animals if animal.type == animal_type]
        for animal in self.animals:
            if animal._animal_type == animal_type:
                animals.append(animal)
        return animals

    def remove_animal_by_id(self, id):
        del self.animals[id]


zoo = Zoo("Zooland")
zoo.add_animal(Animal("Bruno", "Giraffe", 10))
zoo.add_animal(Animal("Popo", "Monkey", 5))
zoo.add_animal(Animal("Miki", "Lion", 7))

tiger = Animal.create_tiger("Felix")
zoo.add_animal(tiger)

for animal in zoo:
    print(animal.name)

print(zoo.get_animal_by_index(0))
print(zoo.remove_animal_by_id(3))
print(len(zoo))







