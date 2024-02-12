#!/usr/bin/python3"""This is the base module for this project"""


from json import dumps, loads


class Base:
    """this is the Base class used for other Objects(Rectangle, square)"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the initialize for instances
        Args:
        id (int|None): it gives an id for each insatnce"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A method that give the JSON string representation of list of dic"""
        if list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method that write JSON string representation of ls_objs to file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """A method that gives the converted obj of json"""
        if json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            my_instance = Rectangle(1, 1)
        elif cls is Square:
            my_instance = Square(1)
        else:
            my_instance = None
        my_instance.update(**dictionary)
        return my_instance

    @classmethod
    def load_from_file(cls):
        """method that load converted json form a file"""
        from os import path
        ff = "{}.json".format(cls.__name__)
        if not path.isfile(ff):
            return []
        with open(ff, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
