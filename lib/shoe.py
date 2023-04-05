#!/usr/bin/env python3

#pytest lib/testing/shoe_test.py -x

import ipdb

class Shoe:
    def __init__(self, brand="assign a brand", color="assign a color", size=0, material="assign material", condition="Used" ):
        self.brand = brand
        self.color = color
        self.size = size
        self.material = material
        self.condition = condition  
        
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if (type(size)==int):
            self._size = size
        else:
            "size must be an integer"
        
    size = property(get_size,set_size)
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
       
# ipdb.set_trace()