#!/usr/bin/python3
"""
abour rectangle
"""
from models.base import Base


class Rectangle(Base):
    ''' this is rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return(self.__width * self.__height)
    
    def display(self):
        for i in range(self.__height):
                print("#"*self.__width)

    @property
    def width(self):
        return self.__width    
    
    @width.setter
    def width(self, a):
        if type(a) != int:
            raise TypeError("width must be an integer")
        if a <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, a):
        if type(a) != int:
            raise TypeError("height must be an integer")
        if a <= 0:
            raise ValueError("height must be > 0")
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, a):
        if type(a) != int:
            raise TypeError("x must be an integer")
        if a < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, a):
        if type(a) != int:
            raise TypeError("y must be an integer")
        if a < 0:
            raise ValueError("y must be >= 0")
