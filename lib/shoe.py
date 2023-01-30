#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand):
        self.brand = brand

    def get_size(self):
        return self._size if hasattr(self, "_size") else None

    def set_size(self, size):
        if(type(size) == int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    size = property(get_size, set_size)

    pass