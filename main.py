from character import Character, Hero, Item
from serialization_pickle import serialize_to_pickle, deserialize_from_pickle

from serialization_json import serialize_to_json, deserialize_from_json, deserialize_object

# lst_one = [1, 2, 3, 4, 5]
# lst_two = lst_one

# lst_two[1] = 9

# print(lst_one)
# print(lst_two)

# hero = Hero("Hero 1", 100)
# sword = Item("Sword", 100.0)
# shield = Item("Shield", 200.0)

# hero.add_item_to_inventory(sword)
# hero.add_item_to_inventory(shield)

# serialize_to_json(hero, 'hero.json')

my_dict = deserialize_from_json("hero.json")

print(deserialize_object(Hero, my_dict))

# serialize_to_pickle(hero, "hero.pkl")

# pickled_hero = deserialize_from_pickle("hero.pkl")
# print(pickled_hero)

