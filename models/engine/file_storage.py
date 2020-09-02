#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            # declare empty return dictionary
            ret = {}
            # if string, destringify the string
            if type(cls) == str:
                cls = eval(cls)
            for key, value in self.__objects.items():
                # Check then add pair to new dictionary
                if cls == type(value):
                    ret[key] = value
            return ret

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def delete(self, obj=None):
        """Deletes object from storage dictionary"""
        if obj is None:
            return
        delet = str(obj.__class__.__name__) + "." + str(obj.id)
        self.all().pop(delet)
        self.save()

    def save(self):
        """Saves storage dictionary to file"""
        temp = {i: self.__objects[i].to_dict() for i in self.__objects.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, "r",) as f:
                for i in json.load(f).values():
                    name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(name)(**i))
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload"""
        self.reload()
