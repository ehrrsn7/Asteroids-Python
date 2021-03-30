"""
File: point.py
Name: Elijah Harrison

Class:      CS 241
Instructor: Brother Mellor

This file contains the Point class.
"""

# include
import math


"""
Class:      Point
components: x (number)
            y (number)
"""
class Point:
    # initializer
    def __init__(self, x_init=0, y_init=0):
        self.x = x_init
        self.y = y_init
    
    """
    Adders
    """
    def add_x(self, dx: float): self.x += dx
    def add_y(self, dy: float): self.y += dy

    def __add__(self, rhs):
        self.x += rhs.x
        self.y += rhs.y
        return self

    def __iadd__(self, rhs):
        return self + rhs

    """
    Setters
    """
    def set_center_point(self):
        self.x = 0
        self.y = 0


"""
UML Class Diagram
----------------------------------
Class: Point
----------------------------------
Components:
+ x // number
+ y // number
----------------------------------
Methods:

Initialize:
+ __init__(x_init=0, y_init=0)

Adders:
+ add_x    (dx: number)
+ add_y    (dy: number)

Operators:
+ __add__(rhs)
+ __iadd__(rhs)
----------------------------------
"""
