#!/usr/bin/python3
""" Defines a Square """


class Square:
    """ Represent a class Square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the class attributes """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Retrieves the private attribute size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the private attribute size to value """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ To retrieve the private attribute position """
        return self.__position

    @position.setter
    def position(self, value):
        """ To set position """
        if not (isinstance(value, tuple) or len(value) != 2 or
                all(isinstance(i, int) or i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
