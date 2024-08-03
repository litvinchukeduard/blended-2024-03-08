from copy import copy, deepcopy


class Person:

    def __init__(self, name, height, age, workplace) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.workplace = workplace

    def __deepcopy__(self, memo):
        for key, value in self.__dict__.items():
            if key != 'workplace':
                pass

    # def __copy__(self):
    #     result = super().__copy__()


person = Person("Ihor", 180, 20, "Home")

# print(dir(person))
print(person.__dict__)

for name, value in person.__dict__.items():
    if name != 'workplace':
        print(f'{name} - {value}')
