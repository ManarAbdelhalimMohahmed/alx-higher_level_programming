#!/usr/bin/python3
"""This is a rectangle module"""


from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class that inherits from a the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """this is the initialize for instance
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): the x-axis coordinate of the rectangle
            y (int): the y-axis coordinate of the rectangle
            id (int|None): the id of the rectangle
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height O .
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < O.
            """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """methon to property gives the width
        Return: the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """a method to set the width"""
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = width

    @property
    def height(self):
        """methon to property gives the height
        Return: the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """a method to set the height"""
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = height

    @property
    def x(self):
        """methon to property gives the x
        Return: the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """a method to set the x"""
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = x

    @property
    def y(self):
        """methon to property gives the y
        Return: the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """a method to set the y"""
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y

    def area(self):
        """a method to get the area of the recangle
        Return: the area."""
        return self.__width * self.__height

    def display(self):
        "a method to display the rectagnle"
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """a method to get info about the clss of instance
        Return: humain readable info"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"
                f" {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """a method to update the attributes of the calss
        It's order goes as the following:
            1- id
            2- width
            3- height
            4- x
            5- y
            """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.__width = args[i]
            if i == 2:
                self.__height = args[i]
            if i == 3:
                self.__x = args[i]
            if i == 4:
                self.__y = args[i]
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "width":
                self.__width = v
            if k == "height":
                self.__height = v
            if k == "x":
                self.__x = v
            if k == "y":
                self.__y = v

    def to_dictionary(self):
        """a method to get the a dic of class attributes
        Return: the dic of its attributes"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
