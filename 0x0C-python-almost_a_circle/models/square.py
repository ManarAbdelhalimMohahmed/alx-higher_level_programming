#!/usr/bin/python3
"""This is a square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Rectangle class that inherits from a the Base class"""
    def __init__(self, size, x=0, y=0, id=None):
        """conatructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """methon to property gives the size
        Return: the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """a method to get info about the clss of instance
        Return: humain readable info"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} -"\
               f" {self.width}"

    def update(self, *args, **kwargs):
        """a method to update the attributes of the calss
        It's order goes as the following:
            1- id
            2- size
            3- x
            4- y
            """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.width = args[i]
                self.height = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "size" or k == "width" or k == "height":
                self.width = v
                self.height = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

    def to_dictionary(self):
        """a method to get the a dic of class attributes
        Return: the dic of its attributes"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
