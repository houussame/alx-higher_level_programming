#!/usr/bin/python3
'''Models for base'''


Class Base:
    '''A representation for base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructer'''
        if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
