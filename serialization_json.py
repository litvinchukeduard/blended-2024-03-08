import json
from datetime import datetime

# {dict: Item, str: datetime}
# def deserialize_object(cls, obj_dict: dict, mapping_dict):
def deserialize_object(cls, obj_dict: dict):
    new_object = cls.__new__(cls)

    for k, v in obj_dict.items():
        # isinstance(v, dict):
        setattr(new_object, k, v) # new_object.name = 'Hero 1'
        # if k in ['creation_date', 'name']
        # if k == 'creation_date':
        #     setattr(new_character, k, datetime.now())
        # else:
        #     setattr(new_character, k, deepcopy(v, memo)) # new_character.'k' = deepcopy(v, memo)

    return new_object

def serialize_object(obj):
    if type(obj) == datetime:
        # return datetime.strftime("%Y-%m-%d %H:%M")
        return str(obj)
    else:
        return obj.__dict__

def serialize_to_json(obj, file_path: str):
    with open(file_path, "w") as file:
        # json.dump(obj, file, default=lambda o: o.__dict__)
        json.dump(obj, file, default=serialize_object)

def deserialize_from_json(file_path: str):
    with open(file_path, "r") as file:
        return json.load(file)
    