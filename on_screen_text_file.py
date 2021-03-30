"""
File: on_screen_text.py
Name: Elijah Harrison

Course:     CS 241
Instructor: Brother Mellor
"""

# include
import arcade
import point_file

# import directory, save all variables we will need
import global_variables_directory as global_variables

"""
This is the class with definitions used by all
on screen text.
"""
class On_Screen_Text:
    def __init__(self,
        text: str           = "",
        font_size: float    = 0):

        self._text      = text
        x               = global_variables.SCREEN_WIDTH
        x               /= 2
        y               = global_variables.SCREEN_HEIGHT
        y               /= 2
        self.p          = point_file.Point(x, y)
        self.font_size  = global_variables.TEXT_NORMAL_FONT_SIZE
        self.color      = global_variables.TEXT_NORMAL_COLOR_DARK

        self.display_text = False

    """
    Properties
    """
    @property
    def text(self): return self._text

    @text.setter
    def text(self, new_text: str): self._text = new_text

    """
    Draw
    """
    def draw(self):
        """
        A default method for easy use by Skeet
        """
        if self.display_text:
            arcade.draw_text(
                self.text       ,
                self.p.x        ,
                self.p.y        ,
                self.color      ,
                self.font_size   )

