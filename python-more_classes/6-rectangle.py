#!/usr/bin/python3
""" lets create a rectangle class"""


class Rectangle:
    """ Initialization"""

    def __init__(self, width=0, height=0):
        """ methods"""
        number_of_instances = 0
        print_symbol ="#"

        self.width = width
        self.height = height

        number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += str(self.print_symbol) * self.width
            if i < self.height - 1:
                result += "\n"
        return result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        number_of_instances -= 1
