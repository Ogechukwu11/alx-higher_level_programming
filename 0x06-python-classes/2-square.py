#I/usr/bin/python3

class Square:
    def __init__(self, size=0):
        try:
            self.__size = size

            raise TypeError("size must be an integer")

        except ValueError("size must be >= 0")
