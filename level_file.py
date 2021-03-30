"""
File:   level.py
Author: Elijah Harrison

This file contains the Level class.
"""

# import
import arcade
import point_file, on_screen_text_file

# import directory, save all variables we will need
import global_variables_directory as global_variables


"""
Class: Level
"""
class Level(on_screen_text_file.On_Screen_Text):
    # initializer
    def __init__(self):
        super().__init__()
        # position
        x           = global_variables.LEVEL_X
        y           = global_variables.LEVEL_Y
        self.p      = point_file.Point(x, y)

        # level (int) container variable
        self.level  = global_variables.LEVEL_INIT

        # display text (bool)
        self.display_text = True

    """
    Methods
    """
    def next_level(self): self.level += 1

    """
    Text
    """
    @property
    def text(self): return f"Level: {self.level}"

    """
    Operators
    """
    def __iadd__(self, rhs: int): self.level += rhs
    def __isub__(self, rhs: int): self.level -= rhs
