from dataclasses import dataclass
from datetime import datetime
from copy import copy, deepcopy

import pickle
"""
Написати клас, який описує персонажа з гри (name, health)
"""
# class Item:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price

#     def __str__(self) -> str:
#         pass

@dataclass(frozen=True)
class Item:
    name: str
    price: float = 1.0

    def __post_init__(self):
        if self.price < 0:
            raise ValueError
        if type(self.price) != float:
            raise ValueError


class Character:
    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name

        self.__health = None
        self.health = health
        self.inventory = []

        self.creation_date = datetime.now()

    def add_item_to_inventory(self, item: Item):
        self.inventory.append(item)

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, new_health):
        # if not isinstance(new_health, int):
        if type(new_health) != int:
            raise ValueError
        if new_health < 0:
            raise ValueError
        self.__health = new_health

    def reduce_health(self, amount: int) -> None:
        self.health -= amount

    '''
    Переписати логіку для копіювання, щоб час створення не передавався у скопійований клас
    '''
    # def __copy__(self):
    #     cls = self.__class__
    #     new_character = cls.__new__(cls)
    #     new_character.__dict__.update(self.__dict__) 
    #     return new_character

    # def __copy__(self):
    #     new_character = Character(self.name, self.health)
    #     new_character.inventory = self.inventory
    #     return new_character
    

    def __copy__(self):
        cls = self.__class__
        new_character = cls.__new__(cls)
        # -------------
        # Our logic:
        dict_copy = copy(self.__dict__)
        # del dict_copy['creation_date']
        dict_copy['creation_date'] = datetime.now()
        # Out logic end
        # -------------
        # new_character.__dict__.update(self.__dict__)
        new_character.__dict__.update(dict_copy)
        return new_character

    def __deepcopy__(self, memo):
        cls = self.__class__
        new_character = cls.__new__(cls)
        memo[id(self)] = new_character

        for k, v in self.__dict__.items():
            # if k in ['creation_date', 'name']
            if k == 'creation_date':
                setattr(new_character, k, datetime.now())
            else:
                setattr(new_character, k, deepcopy(v, memo)) # new_character.'k' = deepcopy(v, memo)

        return new_character

    def __str__(self):
        return f'Character(name = {self.name}, health = {self.health}, inventory = {self.inventory})'
    
    @staticmethod
    def deserialize_from_pickle(file_path):
        with open(file_path, "rb") as file:
            return pickle.load(file)
        
    @classmethod
    def create_new_hero(cls):
        new_hero = cls.__new__(cls)
        new_hero.name = "Hero 2"
        return new_hero

class Hero(Character):
    pass


# hero = Hero("Hero 1", 100)

# hero = Hero.deserialize_from_pickle("hero.pkl")
# print(hero)
hero = Hero.create_new_hero()
print(hero)

# setattr(hero, "name", "Hero 2") # hero.name = "Hero 2"
# print(hero.name)
# print(id(3))

# print(hero.__dict__)

# # my_dict = {}
# # my_dict.update({'key': 1})
# # print(my_dict)


# sword = Item("Sword", 100.0)
# shield = Item("Shield", 200.0)

# hero.add_item_to_inventory(sword)
# hero.add_item_to_inventory(shield)

# # print(hero.inventory)

# hero_copy = copy(hero)

# knife = Item('Knife', 10.0)
# hero.add_item_to_inventory(knife)

# # print(hero.creation_date)
# # print(hero_copy.creation_date)

# print(hero.inventory)
# print(hero_copy.inventory)

# print(dir(hero.__class__))
# print(item)
# item.price = -100.0

# character = Character("Hero", 100)

# character_hero = Hero("Hero 1")
# print(isinstance(character_hero, Character))
# print(character)

# print(character.name)
# character.name = "Hero 2"

# print(character._name)
# print(dir(character))
# print(character._Character__health)
# print(character.__health)
# character.__health = 102
# print(character.__health)

# character.health = "-100"
# character.reduce_health(10)
# print(character.health)
# try:
#     character.health = -100
# except ValueError:
#     print("Error!")
# print(character.health)

# character.health = "-100"
# character.health = True
# print(character.health)

# True False 1 0

# 1 0 

# cls = hero.__class__
# new_character = cls.__new__(cls)
# # print(new_character.name)
# new_character.reduce_health(20)


# hero = Hero("Hero 1", 100)

# hero_deepcopy = deepcopy(hero)

# print(hero.creation_date)
# print(hero_deepcopy.creation_date)
