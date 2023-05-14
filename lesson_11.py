#task1 Напишите генератор, который будет генерировать числа от 0 до бесконечности и вызовите его несколько раз
def num_generator():
    i = 0
    while True:
        yield i
        i += 1

numbers = num_generator()

for i in range(3):
    print(next(numbers))

#task2 Напишите итератор, который будет генерировать числа от 0 до заданного (по сути реализовать функцию range только в виде итератора)
class Num_range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            result = self.start
            self.start += 1
            return result
        else:
            raise StopIteration

numbers = Num_range(0, 10)
for i in numbers:
    print(i)

#task3Допишите класс Family таким образом чтобы он влялся итератором и мы могли при помощи цикла for вывести всех ченов семьи
class Family:

    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members
        self.index = 0

    def __len__(self):
        return len(self.members)

    def add_family_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"Family: last_name - {self.last_name}, count - {len(self.members)}"
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.members):
            result = self.members[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
#task4 Допишите классы таким образом чтобы у FamilyMember был id и в классе Family мы могли найти member по id
class FamilyMember:

    def __init__(self, name, role=None, age=None, id=int):
        self.name = name
        self.role = role
        self.age = age
        self.id = id
    def add_family_member(self, member):
        self.members.append(member)
    def find_family_member_by_id(self,id):
        for member in self.members:
            if member.id == id:
                return member
            return None
    def __len__(self):
        return len(self.members)
    def __str__(self):
        return f"FamilyMember: {self.name}, role: {self.role}, id : {self.id}"


son = FamilyMember(name="Roma", role="son", id = 1)
father = FamilyMember(name="Nikita", role="father", age=43, id = 2)

members = [son, father]
family = Family(last_name="Гаврильчик", members=members)

for members in family:
    print(members)

member = FamilyMember.find_family_member_by_id(2)
if member is not None:
    print(f"find family member with id {members.id}: {members.name}")
else:
    print("Family member not found")
