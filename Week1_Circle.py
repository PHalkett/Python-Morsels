# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:10:57 2020

@author: pjhal
"""
#Week 1: Make a class that represents a circle (radius, diameter, area)

import math

class circle:
    
    def __init__(self, radius=1):
        self.radius = radius
        #self.area = math.pi * self.radius ** 2 for area
        #self.diameter = self.radius * 2 for diameter
        
    def __repr__(self):
        return f"Circle({self.radius})"

#Note: we don't need to implement __str__ (the other string rep.) since it relies on __repr__.

#Bonus 1: When we change the radius, the diameter and area change automatically (make them properties).

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def diameter(self):
        return self.radius * 2

#Bonus 2: The diameter property can be set to a value and the radius will change automatically based on that value.
#Additionally, make area unsettable. Easiest way is to not make a setter at all, duh.

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

#Bonus 3: The radius attribute cannot be set to a negative number (radius can be powered by a property as well)

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

'''
Alternate Method for Bonus 2:
    
    def get_diameter(self):
        return self.radius * 2

    def set_diameter(self, diameter):
        self.radius = diameter / 2

    diameter = property(get_diameter, set_diameter)
    
'''