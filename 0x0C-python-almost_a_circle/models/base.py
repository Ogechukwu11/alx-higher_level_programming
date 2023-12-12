#!/usr/bin/python3

""" This is the base of all classes """
class Base:
    """ creating a private class attribute """
    __nb_objects = 0
    """ Initializing the class constructor attributes
    """
    def __init__(self, id=None):
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
