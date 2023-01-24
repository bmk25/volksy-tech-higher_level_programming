#!/usr/bin/python3
""" abour rectangle """
from base import Base


class Rectangle(Base):
    ''' this is rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, a):
        pass

    @height.setter
    def height(self, a):
        pass
    @x.setter
    def x(self, a):
        pass

    @y.setter
    def y(self, a):
        pass
