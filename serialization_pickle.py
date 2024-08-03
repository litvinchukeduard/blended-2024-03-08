import pickle

def serialize_to_pickle(obj, file_path: str):
    with open(file_path, "wb") as file:
        pickle.dump(obj, file)

def deserialize_from_pickle(file_path: str):
    with open(file_path, "rb") as file:
        return pickle.load(file)
    
    